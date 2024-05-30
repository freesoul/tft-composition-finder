import time
import random
from copy import deepcopy
import dataclasses
from typing import Set, Dict, List, Optional
from champions import TFT_CHAMPIONS, Champion
from traits import TRAIT_BREAKPOINTS_DICT, Trait
from config import (
    MIN_DIFFERENT_TRAITS_PER_LEVEL,
    INCLUDE_CHAMPS,
    EXCLUDE_CHAMPS,
    INCLUDE_TRAITS,
    KEEP_N_BEST,
    TRAIT_SCORE_WEIGHT,
    MIN_MAX_UNIT_BY_COST,
    MAX_ATTEMPTS,
    MIN_SCORE,
    MIN_TRAIT_LEVEL,
    UNIT_SCORE,
)

random.seed(time.time())


@dataclasses.dataclass
class Emblems:
    name: str
    num: int

    @classmethod
    def from_str(cls, emblem_str: str) -> "Emblems":
        name, num = emblem_str.split("_")
        return cls(name=name.lower(), num=int(num))


@dataclasses.dataclass
class Composition:
    champions: Set[Champion]
    emblems: Dict[int, str]

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
            if trait.lower() in self.emblems:
                count += self.emblems[trait.lower()]
            for step in reversed(list(TRAIT_BREAKPOINTS_DICT[trait].steps)):
                if count >= step:
                    res[trait] = step
                    break
        return res

    @property
    def key(self) -> str:
        # TODO: why cost is not an int??
        return ",".join(champion.name for champion in sorted(self.champions, key=lambda x: (int(x.cost), x.name)))  
        



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
            trait_key = f"{trait}_{breakpoint_num}"
            try:
                score += TRAIT_SCORE_WEIGHT[trait_key] * breakpoint_num
            except KeyError:
                score += breakpoint_num

        for champ in self.champions:
            if champ.name in UNIT_SCORE:
                score += UNIT_SCORE[champ.name]
        return score

    def pretty_print(self):
        """
        Prints the composition, and each trait active with its highest breakpoint
        """
        msg = f"Composition: {self.key} - Score {self.score} - Cost {self.total_cost} - "
        traits = []
        for trait, count in self.traits_with_breakpoints.items():
            traits.append((trait, count))
        traits = sorted(traits, key=lambda x: x[1], reverse=True)
        msg += ",".join([f"{trait} {step}" for trait, step in traits])
        print(msg)

    @property
    def max_trait_level(self) -> int:
        max_lvl = 0
        for level in self.traits_with_breakpoints.values():
            if level > max_lvl:
                max_lvl = level
        return max_lvl


class Composer:

    def __init__(self, target_team_size: int = 8, emblems: List[Emblems] = []) -> None:
        self._target_team_size = target_team_size
        self._emblems = emblems
        self._emblems_dict: Dict[str, int] = {emblem.name: emblem.num for emblem in emblems}
        self._found_compositions: List[Composition] = []
        self._found_composition_keys: Set[str] = set()
        self._search_champs = TFT_CHAMPIONS
        for champ in EXCLUDE_CHAMPS:
            self._search_champs = [c for c in self._search_champs if c.name != champ]
        for champ in INCLUDE_CHAMPS:
            if isinstance(champ, str):
                self._search_champs = [c for c in self._search_champs if c.name != champ]

    def compose(self, composition: Optional[Composition] = None, depth: int = 0) -> None:

        if composition is None:
            composition = Composition(champions=set(), emblems=self._emblems_dict)

        num_champs = len(composition.champions)
        new_num_champs = num_champs + 1

        if new_num_champs > self._target_team_size:
            return

        if not self._has_required_champs(composition):
            search_champs = self._pick_missing_champs(composition)
        else:
            search_champs = self._search_champs

        random.shuffle(search_champs)

        max_iterations_idx = max(num_champs - len(INCLUDE_CHAMPS), 0)

        max_iterations = MAX_ATTEMPTS[max_iterations_idx]

        for i, champion in enumerate(search_champs):

            if max_iterations and i > max_iterations:
                break

            if champion in composition.champions:
                continue

            new_composition = Composition(deepcopy(composition.champions).union({champion}), emblems=self._emblems_dict)

            new_composition_num_traits = len(new_composition.traits)

            for num_champs, min_num_traits in MIN_DIFFERENT_TRAITS_PER_LEVEL.items():
                if new_num_champs >= num_champs and new_composition_num_traits < min_num_traits:
                    continue

            # if new_composition.total_cost > MAX_UNIT_COSTS:
            #     continue

            key = new_composition.key

            if key in self._found_composition_keys:
                continue

            if new_num_champs >= 2:
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

                if has_required_traits and has_n_costs_in_range and new_composition.score >= MIN_SCORE and new_composition.max_trait_level >= MIN_TRAIT_LEVEL:

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

    def _has_required_champs(self, composition: Composition) -> bool:
        for req_champ in INCLUDE_CHAMPS:
            if isinstance(req_champ, str):
                if req_champ not in composition.key:
                    return False
            elif isinstance(req_champ, tuple):
                if not any(champ in composition.key for champ in req_champ):
                    return False
        return True

    def _pick_missing_champs(self, composition: Composition) -> List[Champion]:
        missing_champs = []
        for req_champ in INCLUDE_CHAMPS:
            if isinstance(req_champ, str):
                if req_champ not in composition.key:
                    missing_champs.append(self.find_champ(req_champ))
            elif isinstance(req_champ, tuple):
                for champ_name in req_champ:
                    if champ_name not in composition.key:
                        missing_champs.append(self.find_champ(champ_name))
        return missing_champs

    def find_champ(self, champ_name: str) -> Champion:
        for champ in self._search_champs:
            if champ.name == champ_name:
                return champ
        raise ValueError(f"Champion {champ_name} not found in search champs")


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--include-champs", type=str)
    parser.add_argument("--team-size", type=int, default=8)
    parser.add_argument("--emblems", type=str)
    args = parser.parse_args()

    if args.emblems:
        emblems = [Emblems.from_str(emblem_str) for emblem_str in args.emblems.split(",")]
    else:
        emblems = []

    composer = Composer(target_team_size=args.team_size, emblems=emblems)

    if len(args.include_champs) > 0:
        champions = set()
        for champ_name in args.include_champs.split(","):
            champions.add(composer.find_champ(champ_name))
        start_comp = Composition(champions=champions, emblems=composer._emblems_dict)
    else:
        start_comp = Composition(champions=set([champ for champ in TFT_CHAMPIONS if champ.name in INCLUDE_CHAMPS]), emblems=composer._emblems_dict)

    result = composer.compose(start_comp)

    print("\nDone. Best compositions:")
    for comp in composer._found_compositions:
        comp.pretty_print()
