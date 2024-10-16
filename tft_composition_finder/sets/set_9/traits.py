from tft_composition_finder.schemas.trait import Trait

TRAIT_BREAKPOINTS = [
    Trait("bruiser", steps={2, 4, 6, 8}),
    Trait("fortune", steps={3, 5, 7}),
    Trait("arcanist", steps={2, 4, 6, 8}),
    Trait("ghostly", steps={2, 4, 6, 8}),
    Trait("inkshadow", steps={3, 5, 7}),
    Trait("behemoth", steps={2, 4, 6}),
    Trait("warden", steps={2, 4, 6}),
    Trait("fated", steps={3, 5, 7}),
    Trait("invoker", steps={2, 4, 6}),
    Trait("umbral", steps={2, 4, 6, 8}),
    Trait("porcelain", steps={2, 4, 6}),
    Trait("duelist", steps={2, 4, 6, 8}),
    Trait("dragonlord", steps={2, 3, 4, 5}),
    Trait("sage", steps={2, 3, 4, 5}),
    Trait("dryad", steps={2, 4, 6}),
    Trait("mythic", steps={3, 5, 7, 10}),
    Trait("sniper", steps={2, 4, 6}),
    Trait("storyweaver", steps={3, 5, 7, 10}),
    Trait("heavenly", steps={2, 3, 4, 5, 6, 7}),
    Trait("reaper", steps={2, 4}),
    Trait("trickshot", steps={2, 4}),
    Trait("altruist", steps={2, 3, 4}),
    Trait("lovers", steps={1}),
    Trait("great", steps={1}),
    Trait("spirit walker", steps={1}),
    Trait("artist", steps={1}),
]


TRAIT_BREAKPOINTS_DICT = {trait.name: trait for trait in TRAIT_BREAKPOINTS}
