import time
import random

# from copy import deepcopy
from typing import Set, Dict, List, Generator

from tft_composition_finder.schemas.emblems import Emblems
from tft_composition_finder.schemas.composition import Composition
from tft_composition_finder.sets.set_12.champions import TFT_CHAMPIONS, Champion
from tft_composition_finder.sets.set_12.config import (
    INCLUDE_CHAMPS,
    EXCLUDE_CHAMPS,
    # INCLUDE_TRAITS,
    # KEEP_N_BEST,
    # MIN_MAX_UNIT_BY_COST,
    # MAX_ATTEMPTS,
    # MIN_SCORE,
    # MIN_TRAIT_LEVEL,
    # MIN_DIFFERENT_TRAITS_PER_LEVEL,
)

random.seed(time.time())


class BaseComposer:

    def __init__(
        self,
        target_final_min_team_size: int = 7,
        target_final_max_team_size: int = 8,
        emblems: List[Emblems] = [],
    ) -> None:
        self._target_final_min_team_size = target_final_min_team_size
        self._target_final_max_team_size = target_final_max_team_size
        self._emblems = emblems
        self._emblems_dict: Dict[str, int] = {
            emblem.name: emblem.num for emblem in emblems
        }
        self._found_compositions: List[Composition] = []
        self._found_composition_keys: Set[str] = set()
        self._searchable_champs = self._load_searchable_champs()

    def _load_searchable_champs(self) -> List[Champion]:
        search_champs = TFT_CHAMPIONS
        for champ in EXCLUDE_CHAMPS:
            search_champs = [c for c in self._search_champs if c.name != champ]
        for champ in INCLUDE_CHAMPS:
            if isinstance(champ, str):
                search_champs = [c for c in self._search_champs if c.name != champ]
        return search_champs

    def compose(self) -> Generator[Composition, None, None]:
        pass
