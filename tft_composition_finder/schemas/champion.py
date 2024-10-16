
import dataclasses
from typing import Literal, Set

@dataclasses.dataclass
class Champion:
    name: str
    traits: Set[str]
    cost: int
    damage_type: Literal["magic", "physical", "mixed"]

    def __hash__(self) -> int:
        return hash(self.name)