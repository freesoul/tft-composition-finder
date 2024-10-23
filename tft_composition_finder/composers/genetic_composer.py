from typing import List, Generator, Tuple
import random
import bisect

from tft_composition_finder.schemas.emblems import Emblems
from tft_composition_finder.schemas.composition import Composition
from tft_composition_finder.schemas.champion import Champion
from tft_composition_finder.sets.set_12.config import (
    INCLUDE_CHAMPS,  # Assume this is a list of champion names (strings)
)
from tft_composition_finder.composers.base_composer import BaseComposer


class GeneticComposer(BaseComposer):

    def __init__(
        self,
        target_team_size: int = 7,
        emblems: List[Emblems] = [],
        required_champs: List[str] = INCLUDE_CHAMPS,  # List of champion names
        fuzzy: int = 0,
        max_cost: int = 5,
        population_size: int = 1000,
        generations: int = 300,
        mutation_rate: float = 0.1,
        crossover_rate: float = 0.8,
    ) -> None:
        super().__init__(target_team_size, emblems, required_champs, fuzzy, max_cost)
        self._population_size = population_size
        self._generations = generations
        self._mutation_rate = mutation_rate
        self._crossover_rate = crossover_rate

    def compose(self) -> Generator[Composition, None, None]:

        population = self._initialize_population()

        for _ in range(self._generations):

            fitness_scores = [comp.score for comp in population]

            for comp, _ in zip(population, fitness_scores):
                if self._maybe_keep_composition(comp):
                    yield comp

            selected = self._selection(population, fitness_scores)

            offspring = self._crossover(selected)

            population = self._mutation(offspring)

    def _initialize_population(self) -> List[Composition]:
        population = []
        attempts = 0
        while len(population) < self._population_size and attempts < self._population_size * 10:
            comp = self._get_random_composition()
            if comp.key not in [c.key for c in population]:
                population.append(comp)
            attempts += 1
        return population

    def _selection(self, population: List[Composition], fitness_scores: List[float]) -> List[Composition]:
        selected = []
        for _ in range(len(population)):
            # Tournament selection
            tournament = random.sample(list(zip(population, fitness_scores)), k=3)
            winner = max(tournament, key=lambda x: x[1])[0]
            selected.append(winner)
        return selected

    def _crossover(self, selected: List[Composition]) -> List[Composition]:
        offspring = []
        for i in range(0, len(selected), 2):
            parent1 = selected[i]
            parent2 = selected[(i + 1) % len(selected)]
            if random.random() < self._crossover_rate:
                child1, child2 = self._crossover_parents(parent1, parent2)
                offspring.extend([child1, child2])
            else:
                offspring.extend([parent1, parent2])
        return offspring

    def _crossover_parents(self, parent1: Composition, parent2: Composition) -> Tuple[Composition, Composition]:
        """
        We will use a weighted random choices from each parent to favoritize most common traits of each champ
        """
        # we need lists to keep order (sets are unordered)
        parent1_champions = list(parent1.champions)
        parent2_champions = list(parent2.champions)

        # Get most common traits
        both_parent_champs = set(parent1_champions + parent2_champions)
        trait_counts = {}
        for champ in both_parent_champs:
            for trait in champ.traits:
                if trait not in trait_counts:
                    trait_counts[trait] = 0
                trait_counts[trait] += 1

        # Determine weights for each parent
        parent_1_weights = []
        for champ in parent1_champions:
            parent_1_weights.append(sum([trait_counts[trait] for trait in champ.traits]))

        # Pick from parent 2
        parent_2_weights = []
        for champ in parent2_champions:
            parent_2_weights.append(sum([trait_counts[trait] for trait in champ.traits]))

        # Create a couple of children
        children = []
        for _ in range(2):
            parent_1_chosen_champs = self.weighted_sample_without_replacement(parent1_champions, weights=parent_1_weights, k=self._target_team_size // 2)
            parent_2_chosen_champs = self.weighted_sample_without_replacement(parent2_champions, weights=parent_2_weights, k=self._target_team_size // 2)

            # Create a child
            child_champs = set(parent_1_chosen_champs + parent_2_chosen_champs)
            child_champs = self._fix_composition(child_champs, fill_from=both_parent_champs)
            children.append(Composition(champions=child_champs, emblems=self._emblems_dict))

        return children[0], children[1]

    def _mutation(self, offspring: List[Composition]) -> List[Composition]:
        for comp in offspring:
            if random.random() < self._mutation_rate:
                self._mutate_composition(comp)
        return offspring

    def _mutate_composition(self, composition: Composition) -> None:
        non_required_champs = [c for c in composition.champions if c not in self._required_champ_objs]
        if not non_required_champs:
            return
        champ_to_replace = random.choice(list(non_required_champs))
        available_champs = set(self._searchable_champs) - composition.champions
        if not available_champs:
            return  # No available champions to add
        new_champ = random.choice(list(available_champs))
        composition.champions.remove(champ_to_replace)
        composition.champions.add(new_champ)

    @staticmethod
    def weighted_sample_without_replacement(population, weights, k):
        assert len(population) == len(weights)
        cum_weights = list(weights)
        for i in range(1, len(cum_weights)):
            cum_weights[i] += cum_weights[i - 1]
        total = cum_weights[-1]
        selected = []
        for _ in range(k):
            r = random.uniform(0, total)
            i = bisect.bisect_right(cum_weights, r)
            if i >= len(population):  # Ensure index is within range
                i = len(population) - 1
            if not population:  # Check if population is empty
                break
            selected.append(population.pop(i))
            weight = weights.pop(i)
            total -= weight
            cum_weights = [w - weight for w in cum_weights[:i]] + [w - weight for w in cum_weights[i:]]
        return selected
