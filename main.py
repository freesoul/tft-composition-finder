import time
import random
from copy import deepcopy
import dataclasses
from typing import Set, Dict, List
from champions import TFT_CHAMPIONS, Champion
from traits import TRAIT_BREAKPOINTS_DICT, Trait
from config import (
    MIN_TEAM_SIZE,
    MAX_TEAM_SIZE,
    # MAX_UNIT_COSTS,
    MIN_DIFFERENT_TRAITS_LVL2,
    MIN_DIFFERENT_TRAITS_LVL3,
    MIN_DIFFERENT_TRAITS_LVL6,
    MIN_DIFFERENT_TRAITS_LVL8,
    INCLUDE_CHAMPS,
    EXCLUDE_CHAMPS,
    INCLUDE_TRAITS,
    KEEP_N_BEST,
    TRAIT_SCORE_WEIGHT,
    MIN_MAX_UNIT_BY_COST,
    MAX_ATTEMPTS_PER_NUM_CHAMPS,
    MIN_SCORE
)

random.seed(time.time())


@dataclasses.dataclass
class Composition:
    champions: Set[Champion]

    @property
    def traits(self) -> Dict[Trait, int]:
        traits = {}
        for champion in self.champions:
            for trait in champion.traits:
                if trait in traits:
                    traits[trait] += 1
                else:
                    traits[trait] = 1
        return traits

    @property
    def traits_with_breakpoints(self) -> Dict[str, int]:
        res: Dict[str, int] = {}
        for trait, count in self.traits.items():
            for step in reversed(list(TRAIT_BREAKPOINTS_DICT[trait].steps)):
                if count >= step:
                    res[trait] = step
                    break

        return res

    @property
    def key(self) -> str:
        return ",".join(sorted([champion.name for champion in self.champions]))

    @property
    def total_cost(self) -> int:
        return sum([champion.cost for champion in self.champions])

    def includes_trait(self, trait: str) -> bool:
        return any(trait in champion.traits for champion in self.champions)

    def get_num_champs_n_cost(self, n_cost: int) -> int:
        return sum([1 for champion in self.champions if champion.cost == n_cost])

    @property
    def score(self) -> float:
        score = 0.0
        for trait, breakpoint_num in self.traits_with_breakpoints.items():
            try:
                score += TRAIT_SCORE_WEIGHT[trait] * breakpoint_num
            except KeyError:
                score += breakpoint_num
        return score

    def pretty_print(self):
        """
        Prints the composition, and each trait active with its highest breakpoint
        """
        print(self.key, self.score)
        for trait, count in self.traits.items():
            for step in reversed(list(TRAIT_BREAKPOINTS_DICT[trait].steps)):
                if count >= step:
                    print(f"{trait} {step}")
                    break


class Composer:

    def __init__(self) -> None:
        self._found_compositions: List[Composition] = []
        self._found_composition_keys: Set[str] = set()
        self._search_champs = TFT_CHAMPIONS
        for champ in EXCLUDE_CHAMPS:
            self._search_champs = [c for c in self._search_champs if c.name != champ]
        for champ in INCLUDE_CHAMPS:
            self._search_champs = [c for c in self._search_champs if c.name != champ]

    def compose(self, composition: Composition = Composition(set()), depth: int = 0) -> None:

        num_champs = len(composition.champions)
        new_num_champs = num_champs + 1

        if new_num_champs > MAX_TEAM_SIZE:
            return

        random.shuffle(self._search_champs)

        max_iterations = MAX_ATTEMPTS_PER_NUM_CHAMPS[new_num_champs] if new_num_champs in MAX_ATTEMPTS_PER_NUM_CHAMPS else None

        for i, champion in enumerate(self._search_champs):

            if max_iterations and i > max_iterations:
                break

            if champion in composition.champions:
                continue

            new_composition = Composition(deepcopy(composition.champions).union({champion}))

            new_composition_num_traits = len(new_composition.traits)

            if new_composition_num_traits < MIN_DIFFERENT_TRAITS_LVL2 and new_num_champs >= 2:
                continue

            if new_composition_num_traits < MIN_DIFFERENT_TRAITS_LVL3 and new_num_champs >= 3:
                continue

            if new_composition_num_traits < MIN_DIFFERENT_TRAITS_LVL6 and new_num_champs >= 6:
                continue

            if new_composition_num_traits < MIN_DIFFERENT_TRAITS_LVL8 and new_num_champs >= 8:
                continue

            # if new_composition.total_cost > MAX_UNIT_COSTS:
            #     continue

            key = new_composition.key

            if key in self._found_composition_keys:
                continue

            if new_num_champs >= MIN_TEAM_SIZE:

                has_required_champs = True
                for req_champ in INCLUDE_CHAMPS:
                    if req_champ not in new_composition.key:
                        has_required_champs = False
                        break

                has_required_traits = True
                for req_trait in INCLUDE_TRAITS:
                    if not new_composition.includes_trait(req_trait):
                        has_required_traits = False
                        break

                has_n_costs_in_range = True
                for cost, min_max in MIN_MAX_UNIT_BY_COST.items():
                    num_champs_n_cost = new_composition.get_num_champs_n_cost(cost)
                    if num_champs_n_cost < min_max[0] or num_champs_n_cost > min_max[1]:
                        has_n_costs_in_range = False
                        break
                
                if has_required_champs and has_required_traits and has_n_costs_in_range and new_composition.score >= MIN_SCORE:

                    if len(self._found_compositions) < KEEP_N_BEST:
                        self._found_compositions.append(new_composition)
                        new_composition.pretty_print()
                    else:
                        if new_composition.score > self._found_compositions[-1].score:
                            self._found_compositions[-1] = new_composition
                            self._found_compositions.sort(key=lambda x: x.score, reverse=True)
                            new_composition.pretty_print()

            self._found_composition_keys.add(key)
            self.compose(new_composition, depth + 1)


if __name__ == "__main__":
    start_comp = Composition(champions=set([champ for champ in TFT_CHAMPIONS if champ.name in INCLUDE_CHAMPS]))
    composer = Composer()
    result = composer.compose(start_comp)
