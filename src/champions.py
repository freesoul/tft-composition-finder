
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

TFT_CHAMPIONS = [
    Champion(name="Ahri", traits={"Arcana", "Scholar"}, cost=2, damage_type="magic"),
    Champion(name="Akali", traits={"Multistriker", "Warrior", "Pyro"}, cost=2, damage_type="magic"),
    Champion(name="Ashe", traits={"Eldritch", "Hunter"}, cost=1, damage_type="physical"),
    Champion(name="Bard", traits={"Sugarcraft", "Preserver"}, cost=4, damage_type="magic"),
    Champion(name="Blitzcrank", traits={"Honeymancy", "Vanguard"}, cost=1, damage_type="physical"),
    Champion(name="Briar", traits={"Shapeshifter", "Eldritch", "Ravenous"}, cost=5, damage_type="physical"),
    Champion(name="Camille", traits={"Multistriker", "Chrono"}, cost=5, damage_type="physical"),
    Champion(name="Cassiopeia", traits={"Witchcraft", "Incantor"}, cost=2, damage_type="magic"),
    Champion(name="Diana", traits={"Bastion", "Frost"}, cost=5, damage_type="magic"),
    Champion(name="Elise", traits={"Shapeshifter", "Eldritch"}, cost=1, damage_type="magic"),
    Champion(name="Ezreal", traits={"Blaster", "Portal"}, cost=3, damage_type="magic"),
    Champion(name="Fiora", traits={"Witchcraft", "Warrior"}, cost=4, damage_type="physical"),
    Champion(name="Galio", traits={"Vanguard", "Mage", "Portal"}, cost=2, damage_type="magic"),
    Champion(name="Gwen", traits={"Warrior", "Sugarcraft"}, cost=4, damage_type="magic"),
    Champion(name="Hecarim", traits={"Bastion", "Portal"}, cost=3, damage_type="magic"),
    Champion(name="Hwei", traits={"Blaster", "Frost"}, cost=3, damage_type="physical"),
    Champion(name="Jax", traits={"Chrono", "Multistriker"}, cost=1, damage_type="physical"),
    Champion(name="Jayce", traits={"Shapeshifter", "Portal"}, cost=1, damage_type="physical"),
    Champion(name="Jinx", traits={"Hunter", "Sugarcraft"}, cost=3, damage_type="physical"),
    Champion(name="Kalista", traits={"Faerie", "Multistriker"}, cost=4, damage_type="physical"),
    Champion(name="Karma", traits={"Chrono", "Incantor"}, cost=4, damage_type="magic"),
    Champion(name="Kassadin", traits={"Multistriker", "Portal"}, cost=2, damage_type="magic"),
    Champion(name="Katarina", traits={"Faerie", "Warrior"}, cost=3, damage_type="physical"),
    Champion(name="Kogmaw", traits={"Honeymancy", "Hunter"}, cost=2, damage_type="physical"),
    Champion(name="Lillia", traits={"Bastion", "Faerie"}, cost=3, damage_type="magic"),
    Champion(name="Milio", traits={"Scholar", "Faerie"}, cost=5, damage_type="magic"),
    Champion(name="Mordekaiser", traits={"Vanguard", "Eldritch"}, cost=3, damage_type="magic"),
    Champion(name="Morgana", traits={"Witchcraft", "Preserver", "Bat Queen"}, cost=5, damage_type="magic"),
    Champion(name="Nami", traits={"Mage", "Eldritch"}, cost=4, damage_type="magic"),
    Champion(name="Nasus", traits={"Shapeshifter", "Pyro"}, cost=4, damage_type="magic"),
    Champion(name="Neeko", traits={"Witchcraft", "Shapeshifter"}, cost=3, damage_type="magic"),
    Champion(name="Nilah", traits={"Warrior", "Eldritch"}, cost=2, damage_type="physical"),
    Champion(name="Nomsy", traits={"Hunter", "Dragon"}, cost=1, damage_type="magic"),
    Champion(name="Norra", traits={"Explorer", "Mage", "Portal"}, cost=5, damage_type="magic"),
    Champion(name="Nunu", traits={"Bastion", "Honeymancy"}, cost=2, damage_type="magic"),
    Champion(name="Olaf", traits={"Hunter", "Frost"}, cost=4, damage_type="physical"),
    Champion(name="Poppy", traits={"Witchcraft", "Bastion"}, cost=1, damage_type="magic"),
    Champion(name="Rakan", traits={"Preserver", "Faerie"}, cost=4, damage_type="magic"),
    Champion(name="Rumble", traits={"Blaster", "Sugarcraft", "Vanguard"}, cost=2, damage_type="physical"),
    Champion(name="Ryze", traits={"Scholar", "Portal"}, cost=4, damage_type="magic"),
    Champion(name="Seraphine", traits={"Mage", "Faerie"}, cost=1, damage_type="magic"),
    Champion(name="Shen", traits={"Bastion", "Pyro"}, cost=3, damage_type="physical"),
    Champion(name="Shyvana", traits={"Shapeshifter", "Dragon"}, cost=2, damage_type="magic"),
    Champion(name="Smolder", traits={"Blaster", "Dragon"}, cost=5, damage_type="physical"),
    Champion(name="Soraka", traits={"Mage", "Sugarcraft"}, cost=1, damage_type="magic"),
    Champion(name="Swain", traits={"Shapeshifter", "Frost"}, cost=3, damage_type="magic"),
    Champion(name="Syndra", traits={"Incantor", "Eldritch"}, cost=2, damage_type="magic"),
    Champion(name="Tahm Kench", traits={"Vanguard", "Arcana"}, cost=4, damage_type="physical"),
    Champion(name="Taric", traits={"Bastion", "Portal"}, cost=4, damage_type="magic"),
    Champion(name="Tristana", traits={"Blaster", "Faerie"}, cost=2, damage_type="physical"),
    Champion(name="Twitch", traits={"Frost", "Hunter"}, cost=1, damage_type="physical"),
    Champion(name="Varus", traits={"Blaster", "Pyro"}, cost=4, damage_type="physical"),
    Champion(name="Veigar", traits={"Mage", "Honeymancy"}, cost=3, damage_type="magic"),
    Champion(name="Vex", traits={"Mage", "Chrono"}, cost=3, damage_type="magic"),
    Champion(name="Warwick", traits={"Frost", "Vanguard"}, cost=1, damage_type="physical"),
    Champion(name="Wukong", traits={"Druid"}, cost=3, damage_type="physical"),
    Champion(name="Xerath", traits={"Arcana", "Ascendant"}, cost=5, damage_type="magic"),
    Champion(name="Ziggs", traits={"Honeymancy", "Incantor"}, cost=1, damage_type="magic"),
    Champion(name="Zilean", traits={"Preserver", "Chrono"}, cost=2, damage_type="magic"),
    Champion(name="Zoe", traits={"Witchcraft", "Scholar", "Portal"}, cost=1, damage_type="magic"),
    Champion(name="Wukong", traits={"Druid"}, cost=3, damage_type="physical"),
]