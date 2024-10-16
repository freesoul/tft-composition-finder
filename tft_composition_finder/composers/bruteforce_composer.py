import time
import random
from copy import deepcopy
from typing import Set, Dict, List, Optional

from tft_composition_finder.schemas.emblems import Emblems
from tft_composition_finder.schemas.composition import Composition
from tft_composition_finder.sets.set_12.champions import TFT_CHAMPIONS, Champion
from tft_composition_finder.sets.set_12.config import (
    MIN_DIFFERENT_TRAITS_PER_LEVEL,
    INCLUDE_CHAMPS,
    EXCLUDE_CHAMPS,
    MAX_ATTEMPTS,
    KEEP_N_BEST,
)

random.seed(time.time())


class Composer:

    def __init__(self, target_team_size: int = 8, emblems: List[Emblems] = []) -> None:
        self._target_team_size = target_team_size
        self._emblems = emblems
        self._emblems_dict: Dict[str, int] = {
            emblem.name: emblem.num for emblem in emblems
        }
        self._found_compositions: List[Composition] = []
        self._found_composition_keys: Set[str] = set()
        self._search_champs = TFT_CHAMPIONS
        for champ in EXCLUDE_CHAMPS:
            self._search_champs = [c for c in self._search_champs if c.name != champ]
        for champ in INCLUDE_CHAMPS:
            if isinstance(champ, str):
                self._search_champs = [
                    c for c in self._search_champs if c.name != champ
                ]

    def compose(
        self, composition: Optional[Composition] = None, depth: int = 0
    ) -> None:

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

            new_composition = Composition(
                deepcopy(composition.champions).union({champion}),
                emblems=self._emblems_dict,
            )

            new_composition_num_traits = len(new_composition.traits)

            for num_champs, min_num_traits in MIN_DIFFERENT_TRAITS_PER_LEVEL.items():
                if (
                    new_num_champs >= num_champs
                    and new_composition_num_traits < min_num_traits
                ):
                    continue

            key = new_composition.key

            if key in self._found_composition_keys:
                continue

            if new_num_champs >= 2:

                if new_composition.score > 0.0:

                    if len(self._found_compositions) < KEEP_N_BEST:
                        self._found_compositions.append(new_composition)
                        new_composition.pretty_print()
                    else:
                        if new_composition.score > self._found_compositions[-1].score:
                            self._found_compositions[-1] = new_composition
                            self._found_compositions.sort(
                                key=lambda x: x.score, reverse=True
                            )
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
        emblems = [
            Emblems.from_str(emblem_str) for emblem_str in args.emblems.split(",")
        ]
    else:
        emblems = []

    composer = Composer(target_team_size=args.team_size, emblems=emblems)

    if len(args.include_champs) > 0:
        champions = set()
        for champ_name in args.include_champs.split(","):
            champions.add(composer.find_champ(champ_name))
        start_comp = Composition(champions=champions, emblems=composer._emblems_dict)
    else:
        start_comp = Composition(
            champions=set(
                [champ for champ in TFT_CHAMPIONS if champ.name in INCLUDE_CHAMPS]
            ),
            emblems=composer._emblems_dict,
        )

    result = composer.compose(start_comp)

    print("\nDone. Best compositions:")
    for comp in composer._found_compositions:
        comp.pretty_print()
