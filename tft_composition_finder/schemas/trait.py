from typing import Set
import dataclasses


@dataclasses.dataclass
class Trait:
    name: str
    steps: Set[int]