
import dataclasses
from typing import Literal, Set


CHAMP_ROLE = Literal["tank", "ad", "ap"]


@dataclasses.dataclass
class Champion:
    name: str
    traits: Set[str]
    cost: int
    roles: Set[CHAMP_ROLE]

    def __hash__(self) -> int:
        return hash(self.name)