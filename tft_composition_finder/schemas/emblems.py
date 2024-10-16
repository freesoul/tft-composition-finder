import dataclasses

@dataclasses.dataclass
class Emblems:
    name: str
    num: int

    @classmethod
    def from_str(cls, emblem_str: str) -> "Emblems":
        name, num = emblem_str.split("_")
        return cls(name=name.lower(), num=int(num))
