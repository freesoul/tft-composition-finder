import time
import random

from copy import deepcopy
from typing import Set, Dict, List, Generator, Union

from tft_composition_finder.schemas.emblems import Emblems
from tft_composition_finder.schemas.composition import Composition
from tft_composition_finder.sets.set_12.champions import TFT_CHAMPIONS, Champion
from tft_composition_finder.sets.set_12.config import (
    INCLUDE_CHAMPS,
    KEEP_N_BEST,
    EXCLUDE_CHAMPS,
)

random.seed(time.time())


class BaseComposer:

    def __init__(
        self,
        target_team_size: int = 7,
        emblems: List[Emblems] = [],
        required_champs: List[str] = INCLUDE_CHAMPS,
        fuzzy: int = 0,
        max_cost: int = 5,
    ) -> None:
        self._target_team_size = target_team_size
        self._emblems = emblems
        self._emblems_dict: Dict[str, int] = {
            emblem.name: emblem.num for emblem in emblems
        }
        self._found_compositions: List[Composition] = []
        self._found_composition_keys: Set[str] = set()
        self._max_cost = max_cost
        self._required_champs = required_champs
        self._searchable_champs = self._get_searchable_champs()
        self._fuzzy = fuzzy
        self._num_required_champs = len(required_champs) - fuzzy

    def compose(self) -> Generator[Composition, None, None]:
        pass

    def _get_searchable_champs(self) -> List[Champion]:
        champs = []
        for champ in TFT_CHAMPIONS:
            if champ.cost > self._max_cost and not champ.name in self._required_champs:
                continue
            if champ.name in EXCLUDE_CHAMPS:
                continue
            if champ.cost is None or not isinstance(champ.cost, (int, float)):
                raise ValueError(
                    f"Champion {champ.name} in searchable champs has invalid cost: {champ.cost}"
                )
            champs.append(champ)
        return champs

    def _has_required_champs(self, composition: Composition) -> bool:
        if self._num_required_champs == 0:
            return True
        count = 0
        for req_champ in self._required_champs:
            if isinstance(req_champ, str):
                if req_champ in composition.key:
                    count += 1
            elif isinstance(req_champ, tuple):
                if any(champ in composition.key for champ in req_champ):
                    count += 1
            if count >= self._num_required_champs:
                return True
        return count >= self._num_required_champs

    def _get_champ(self, champ_name: str) -> Champion:
        for champ in self._searchable_champs:
            if champ.name == champ_name:
                return champ
        raise ValueError(f"Champion {champ_name} not found in search champs")

    def _maybe_keep_composition(self, composition: Composition) -> bool:
        kept = False
        score = composition.score  # calculate once
        if score > 0.0:
            if len(self._found_compositions) < KEEP_N_BEST:
                self._found_compositions.append(composition)
                # composition.pretty_print()
                kept = True
            elif score > self._found_compositions[-1].score:
                self._found_compositions[-1] = composition
                self._found_compositions.sort(key=lambda x: x.score, reverse=True)
                # composition.pretty_print()
                kept = True
        self._found_composition_keys.add(composition.key)
        return kept

    def _pick_missing_required_champs(self, composition: Composition) -> List[Champion]:
        missing_champs = []
        for req_champ in random.sample(
            self._required_champs, k=self._num_required_champs
        ):
            if isinstance(req_champ, str):
                if req_champ not in composition.key:
                    missing_champs.append(self._get_champ(req_champ))
            elif isinstance(req_champ, tuple):
                for champ_name in req_champ:
                    if champ_name not in composition.key:
                        missing_champs.append(self._get_champ(champ_name))
        return missing_champs

    def _get_next_sampleable_champs(
        self, composition: Composition
    ) -> List[Champion]:
        if not self._has_required_champs(composition):
            search_champs = self._pick_missing_required_champs(composition)
        else:
            search_champs = self._searchable_champs
        return search_champs

    def _generate_possible_champs(
        self, composition: Composition
    ) -> Generator[Champion, None, None]:
        if not self._has_required_champs(composition):
            for champ in self._pick_missing_required_champs(composition):
                yield champ

        copy_champs = deepcopy(self._searchable_champs)

        random.shuffle(copy_champs)

        for champ in copy_champs:
            if champ.name not in composition.key:
                yield champ

    def _get_random_composition(self) -> Composition:
        champs: Set[Champion] = set()
        i = 0
        for champ in self._generate_possible_champs(Composition(set(), self._emblems_dict)):
            champs.add(champ)
            i += 1
            if i >= self._target_team_size:
                break

        composition = Composition(champions=champs, emblems=self._emblems_dict)
        return composition
