from typing import Set, Dict
import dataclasses

from tft_composition_finder.sets.set_12.champions import Champion
from tft_composition_finder.sets.set_12.traits import TRAIT_BREAKPOINTS_DICT, Trait


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
        return ",".join(
            champion.name
            for champion in sorted(self.champions, key=lambda x: (int(x.cost), x.name))
        )

    @property
    def cost(self) -> int:
        return sum([champion.cost for champion in self.champions])

    def includes_trait(self, trait: str) -> bool:
        return any(trait in champion.traits for champion in self.champions)

    def get_num_champs_with_n_cost(self, n_cost: int) -> int:
        return sum([1 for champion in self.champions if champion.cost == n_cost])

    @property
    def score(self) -> float:
        # For now this is here to prevent the circular import of Composition -> fitness -> Composition
        # TODO: refacto so that either we don't use .score
        from tft_composition_finder.fitness import fitness
        return fitness(self)

    def pretty_print(self):
        """
        Prints the composition, and each trait active with its highest breakpoint
        """
        msg = (
            f"Composition: {self.key} - Score {self.score} - Cost {self.cost} - "
        )
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

    def __add__(self, other):
        return Composition(
            champions=self.champions.union(other.champions),
            emblems=self.emblems,
        )
    
    def __and__(self, other):
        return Composition(
            champions=self.champions.intersection(other.champions),
            emblems=self.emblems,
        )
    
    def __sub__(self, other):
        return Composition(
            champions=self.champions.difference(other.champions),
            emblems=self.emblems,
        )
    