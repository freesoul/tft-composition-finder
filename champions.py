
import dataclasses
from typing import Literal, Set

@dataclasses.dataclass
class Champion:
    name: str
    traits: Set[str]
    cost: int
    damage_type: Literal["magic", "physical", "mixed"]
    ability: str

    def __hash__(self) -> int:
        return hash(self.name)

TFT_CHAMPIONS = [
    Champion(name="Aatrox", traits={"bruiser", "ghostly", "inkshadow"}, cost=2, damage_type="magic", ability="shred current target, deal dmg, heal self"),
    Champion(name="Ahri", traits={"arcanist", "fated"}, cost=1, damage_type="magic", ability="deal dmg to current target + adjacent enemies"),
    Champion(name="Alune", traits={"invoker", "umbral"}, cost=3, damage_type="magic", ability="dmg + shred row with most enemy health, buff ally stats: grant AS to allies in her row"),
    Champion(name="Amumu", traits={"porcelain", "warden"}, cost=3, damage_type="magic", ability="heal self, heal allies, + deal dmg"),
    Champion(name="Annie", traits={"fortune", "invoker"}, cost=4, damage_type="magic", ability="stun, deal dmg, burn, wound enemies; heal self when damaging burning enemy"),
    Champion(name="Aphelios", traits={"fated", "sniper"}, cost=3, damage_type="physical", ability="sunder enemies, deal dmg"),
    Champion(name="Ashe", traits={"porcelain", "sniper"}, cost=4, damage_type="physical", ability="stacking dmg"),
    Champion(name="Azir", traits={"dryad", "invoker"}, cost=5, damage_type="magic", ability="fire beam, dealing dmg, spawn target dummy next to first enemy hit"),
    Champion(name="Bard", traits={"mythic", "trickshot"}, cost=3, damage_type="mixed", ability="deal +dmg"),
    Champion(name="Caitlyn", traits={"ghostly", "sniper"}, cost=1, damage_type="physical", ability="deal dmg to first enemy hit on way to further enemy"),
    Champion(name="Cho'gath", traits={"behemoth", "mythic"}, cost=1, damage_type="magic", ability="shield self, deal dmg, burn, wound enemies"),
    Champion(name="Darius", traits={"duelist", "umbral"}, cost=1, damage_type="magic", ability="deal dmg to adjacent enemies + on-hit extra dmg"),
    Champion(name="Diana", traits={"dragonlord", "sage"}, cost=3, damage_type="magic", ability="tank (take reduced dmg) from enemies >1 hex away + on-hit extra dmg"),
    Champion(name="Galio", traits={"bruiser", "storyweaver"}, cost=4, damage_type="magic", ability="taunt enemies within 3 hexes, tank (+armour, + MR), then deal dmg and shield allies"),
    Champion(name="Garen", traits={"storyweaver", "warden"}, cost=1, damage_type="physical", ability="shield self + on-hit extra dmg"),
    Champion(name="Gnar", traits={"dryad", "warden"}, cost=2, damage_type="physical", ability="gain stacking AD, deal dmg to enemies in a line"),
    Champion(name="Hwei", traits={"artist", "mythic"}, cost=5, damage_type="magic", ability="heal allies and deals dmg to enemies in a zone"),
    Champion(name="Illaoi", traits={"arcanist", "ghostly", "warden"}, cost=3, damage_type="magic", ability="shield self, spawn tentacle dealing dmg and heal self"),
    Champion(name="Irelia", traits={"duelist", "storyweaver"}, cost=5, damage_type="physical", ability="deal dmg and sunder enemies, especially lowest-health enemies; converts bonus AS into AD"),
    Champion(name="Janna", traits={"dragonlord", "invoker"}, cost=2, damage_type="magic", ability="shield allies: 2 lowest-health allies, dmg to 2 nearest enemies"),
    Champion(name="Jax", traits={"inkshadow", "warden"}, cost=1, damage_type="magic", ability="tank (+armour, + MR), then deal dmg + stun current target, and dmg adjacent targets"),
    Champion(name="Kai'sa", traits={"inkshadow", "trickshot"}, cost=4, damage_type="physical", ability="fire at current target, deal dmg to first enemy hit, more if they've been hit 10 times"),
    Champion(name="Kayn", traits={"ghostly", "reaper"}, cost=4, damage_type="physical", ability="transform, gain crit chance + dmg, more dmg to isolated targets"),
    Champion(name="Kha'zix", traits={"heavenly", "reaper"}, cost=1, damage_type="physical", ability="dmg lowest-health enemy within 3 hexes"),
    Champion(name="Kindred", traits={"dryad", "fated", "reaper"}, cost=2, damage_type="magic", ability="dash, deal dmg to current target + nearest enemy"),
    Champion(name="Kobuko", traits={"bruiser", "fortune"}, cost=1, damage_type="magic", ability="heal self and deal +dmg according to HP (passive: gain permanent HP per interest gold)"),
    Champion(name="Kog'maw", traits={"invoker", "mythic", "sniper"}, cost=1, damage_type="magic", ability="dmg lowest-health enemy in range, gain +1 range every 2 casts"),
    Champion(name="Lee Sin", traits={"dragonlord", "duelist"}, cost=4, damage_type="physical", ability="deal dmg, mana reave, stun target, and enemies on the way. shield self"),
    Champion(name="Lillia", traits={"invoker", "mythic"}, cost=4, damage_type="magic", ability="deal dmg to enemy in area, then to enemies behind"),
    Champion(name="Lissandra", traits={"arcanist", "porcelain"}, cost=5, damage_type="magic", ability="deal dmg. if enemy dies, chance of loot; otherwise, dmg largest group of enemies"),
    Champion(name="Lux", traits={"arcanist", "porcelain"}, cost=2, damage_type="magic", ability="deal dmg along way to further enemy, stun first 2 enemies"),
    Champion(name="Malphite", traits={"behemoth", "heavenly"}, cost=1, damage_type="magic", ability="tank (+armour) and deal dmg to enemies in a cone"),
    Champion(name="Morgana", traits={"ghostly", "sage"}, cost=4, damage_type="magic", ability="deal dmg + chill largest clump on enemies"),
    Champion(name="Nautilus", traits={"mythic", "warden"}, cost=4, damage_type="magic", ability="deal dmg + stun most enemies in a line"),
    Champion(name="Neeko", traits={"arcanist", "heavenly", "mythic"}, cost=2, damage_type="magic", ability="tank (take reduced dmg) + heal self, then deal dmg to adjacent enemies"),
    Champion(name="Ornn", traits={"behemoth", "dryad"}, cost=4, damage_type="magic", ability="shield self, unstoppable, deal dmg to adjacent enemies + buff ally (temp item)"),
    Champion(name="Qiyana", traits={"duelist", "heavenly"}, cost=2, damage_type="physical", ability="deal +dmg to target and enemies behind them"),
    Champion(name="Rakan", traits={"altruist", "dragonlord", "lovers"}, cost=5, damage_type="magic", ability="deal dmg + reduce dmg of largest group of enemies, shield self"),
    Champion(name="Rek'sai", traits={"bruiser", "dryad"}, cost=1, damage_type="magic", ability="tank (+armour, + MR), stun + dmg nearby enemies"),
    Champion(name="Riven", traits={"altruist", "bruiser", "storyweaver"}, cost=2, damage_type="physical", ability="deal dmg, every 3rd cast also dmg adjacent enemies + heal self"),
    Champion(name="Senna", traits={"inkshadow", "sniper"}, cost=2, damage_type="physical", ability="damage enemies behind current target, grant AD to adjacent allies"),
    Champion(name="Sett", traits={"fated", "umbral", "warden"}, cost=5, damage_type="physical", ability="stun + dmg target, dmg enemies as % of target's HP (passive: squat allies. no tl;dr.)"),
    Champion(name="Shen", traits={"behemoth", "ghostly"}, cost=2, damage_type="mixed", ability="tank (take reduced dmg) for shen + adjacent allies, deal bonus true dmg (based on armour)"),
    Champion(name="Sivir", traits={"storyweaver", "trickshot"}, cost=1, damage_type="physical", ability="buff ally stats: +AD and +AS to self and adjacent allies"),
    Champion(name="Soraka", traits={"altruist", "heavenly"}, cost=3, damage_type="magic", ability="mana reave + dmg largest group of enemies (passive: gain AP as team loses % health)"),
    Champion(name="Sylas", traits={"bruiser", "umbral"}, cost=4, damage_type="magic", ability="dmg target and nearby enemies, heal self"),
    Champion(name="Syndra", traits={"arcanist", "fated"}, cost=4, damage_type="magic", ability="deal dmg to target, increasing per cast"),
    Champion(name="Tahm Kench", traits={"bruiser", "mythic"}, cost=3, damage_type="magic", ability="shield self & dmg current target; +dmg if tahm kench has more health than them"),
    Champion(name="Teemo", traits={"fortune", "trickshot"}, cost=2, damage_type="magic", ability="poison (dmg) closest non-poisoned enemy"),
    Champion(name="Thresh", traits={"behemoth", "fated"}, cost=3, damage_type="magic", ability="thresh + lowest-health ally tank (shield allies & share armour & MR), dmg adjacent enemies"),
    Champion(name="Tristana", traits={"duelist", "fortune"}, cost=3, damage_type="physical", ability="gain AD, jump on target and dmg adjacent enemies"),
    Champion(name="Udyr", traits={"behemoth", "inkshadow", "spirit walker"}, cost=5, damage_type="magic", ability="shield self, knock up and damage enemies / gain AS and dmg"),
    Champion(name="Volibear", traits={"duelist", "inkshadow"}, cost=3, damage_type="magic", ability="3 empowered attacks: 2 heal self + dmg, 1 stuns + dmg"),
    Champion(name="Wukong", traits={"great", "heavenly"}, cost=5, damage_type="physical", ability="cycle through abilities: dmg + stun; dmg adjacent enemies; dash to + dmg enemies in a line"),
    Champion(name="Xayah", traits={"dragonlord", "lovers", "trickshot"}, cost=5, damage_type="physical", ability="dmg 4 closest enemies, and enemies on the way"),
    Champion(name="Yasuo", traits={"duelist", "fated"}, cost=1, damage_type="magic", ability="shield self + dmg; attacks while shielded deal bonus dmg"),
    Champion(name="Yone", traits={"reaper", "umbral"}, cost=3, damage_type="physical", ability="dash to furthest enemy within 3 hex, dmg + wound along the way; shield self + AS"),
    Champion(name="Yorick", traits={"behemoth", "umbral"}, cost=2, damage_type="magic", ability="gain max health and deal dmg to 2 nearest enemies"),
    Champion(name="Zoe", traits={"arcanist", "fortune", "storyweaver"}, cost=3, damage_type="magic", ability="dmg current target, missile ricochets to furthest unit within 2 hexes; + ricochets per kill"),
    Champion(name="Zyra", traits={"sage", "storyweaver"}, cost=2, damage_type="magic", ability="summon 2 plans that dmg and wound target"),
]

