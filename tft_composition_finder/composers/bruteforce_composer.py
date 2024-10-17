from copy import deepcopy
from typing import List, Optional, Generator

from tft_composition_finder.schemas.emblems import Emblems
from tft_composition_finder.schemas.composition import Composition
from tft_composition_finder.sets.set_12.config import (
    INCLUDE_CHAMPS,
    MAX_ATTEMPTS,
)
from tft_composition_finder.composers.base_composer import BaseComposer

class BruteforceComposer(BaseComposer):

    def __init__(
        self,
        target_team_size: int = 7,
        emblems: List[Emblems] = [],
    ) -> None:
        super().__init__(target_team_size, emblems)

    def compose(self, composition: Optional[Composition] = None, depth: int = 0) -> Generator[Composition, None, None]:

        # First iteration
        if composition is None:
            composition = Composition(champions=set(), emblems=self._emblems_dict)

        # We add one champion on each recursive call
        num_champs = len(composition.champions)
        new_composition_num_champs = num_champs + 1
        if new_composition_num_champs > self._target_team_size:
            return

        # Select the champions from which to search
        search_champs = self._get_next_sampleable_champs(composition)

        # Iterate over the champions and test the compositions
        max_iterations_idx = max(num_champs - len(INCLUDE_CHAMPS), 0)

        max_iterations = MAX_ATTEMPTS[max_iterations_idx]

        for i, champion in enumerate(search_champs):

            if max_iterations and i > max_iterations:
                break

            if champion in composition.champions:
                continue

            # Create a new composition with the new champion
            new_composition = Composition(
                deepcopy(composition.champions).union({champion}),
                emblems=self._emblems_dict,
            )

            # Skip if already added
            if new_composition.key in self._found_composition_keys:
                continue

            # Keep the composition
            if new_composition_num_champs >= 2 and self._maybe_keep_composition(new_composition):
                yield new_composition

            # Delegate the yielding of deeper compositions to the next recursive call
            yield from self.compose(new_composition, depth + 1)
