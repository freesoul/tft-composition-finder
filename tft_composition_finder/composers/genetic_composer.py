from copy import deepcopy
from typing import List, Optional, Generator, Tuple
import random

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
        population_size: int = 800,
        generations: int = 200,
        mutation_rate: float = 0.1,
        crossover_rate: float = 0.7,
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
        while (
            len(population) < self._population_size
            and attempts < self._population_size * 10
        ):
            comp = self._get_random_composition()
            if comp.key not in [c.key for c in population]:
                population.append(comp)
            attempts += 1
        return population

    def _selection(
        self, population: List[Composition], fitness_scores: List[float]
    ) -> List[Composition]:
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

    def _crossover_parents(
        self, parent1: Composition, parent2: Composition
    ) -> Tuple[Composition, Composition]:
        parent1_champs = list(parent1.champions)
        parent2_champs = list(parent2.champions)
        crossover_point = random.randint(1, self._target_team_size - 1)

        child1_champs = parent1_champs[:crossover_point]
        child2_champs = parent2_champs[:crossover_point]

        # Add unique champions from the other parent
        for champ in parent2_champs:
            if (
                champ not in child1_champs
                and len(child1_champs) < self._target_team_size
            ):
                child1_champs.append(champ)
        for champ in parent1_champs:
            if (
                champ not in child2_champs
                and len(child2_champs) < self._target_team_size
            ):
                child2_champs.append(champ)

        # Ensure required champions are included
        required_champions = set(
            self._get_champ(name) for name in self._required_champs
        )
        child1_champs = set(child1_champs).union(required_champions)
        child2_champs = set(child2_champs).union(required_champions)

        # Fix compositions to ensure correct team size and uniqueness
        child1_champs = self._fix_champions(child1_champs)
        child2_champs = self._fix_champions(child2_champs)

        child1 = Composition(champions=child1_champs, emblems=self._emblems_dict)
        child2 = Composition(champions=child2_champs, emblems=self._emblems_dict)
        return child1, child2

    def _fix_champions(self, champs: set) -> set:
        champs = set(champs)
        required_champions = set(
            self._get_champ(name) for name in self._required_champs
        )
        champs.update(required_champions)
        # Remove excess champions
        while len(champs) > self._target_team_size:
            non_required_champs = champs - required_champions
            if non_required_champs:
                champ_to_remove = random.choice(list(non_required_champs))
                champs.remove(champ_to_remove)
            else:
                break  # Cannot remove required champions
        # Add missing champions
        while len(champs) < self._target_team_size:
            champs.add(
                next(
                    self._generate_possible_champs(
                        Composition(champs, self._emblems_dict)
                    )
                )
            )
        return champs

    def _mutation(self, offspring: List[Composition]) -> List[Composition]:
        for comp in offspring:
            if random.random() < self._mutation_rate:
                self._mutate_composition(comp)
        return offspring

    def _mutate_composition(self, composition: Composition) -> None:
        required_champions = set(
            self._get_champ(name) for name in self._required_champs
        )
        non_required_champs = [
            c for c in composition.champions if c not in required_champions
        ]
        if not non_required_champs:
            return
        champ_to_replace = random.choice(list(non_required_champs))
        available_champs = set(self._searchable_champs) - composition.champions
        if not available_champs:
            return  # No available champions to add
        new_champ = random.choice(list(available_champs))
        composition.champions.remove(champ_to_replace)
        composition.champions.add(new_champ)
