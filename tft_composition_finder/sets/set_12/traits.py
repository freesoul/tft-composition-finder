from tft_composition_finder.schemas.trait import Trait

TRAIT_BREAKPOINTS = [
    Trait("Arcana", steps={2, 3, 4, 5}),
    Trait("Ascendant", steps={2, 3}),
    Trait("Bastion", steps={2, 4, 6, 8}),
    Trait("Blaster", steps={2, 4, 6}),
    Trait("Dragon", steps={2, 3}),
    Trait("Eldritch", steps={3, 5, 7, 10}),
    Trait("Faerie", steps={3, 5, 7, 9}),
    Trait("Frost", steps={3, 5, 7, 9}),
    Trait("Honeymancy", steps={3, 5, 7}),
    Trait("Hunter", steps={2, 4, 6}),
    Trait("Incantor", steps={2, 4}),
    Trait("Mage", steps={3, 5, 7, 10}),
    Trait("Multistriker", steps={3, 5, 7, 9}),
    Trait("Portal", steps={3, 6, 8, 10}),
    Trait("Pyro", steps={2, 3, 4, 5}),
    Trait("Scholar", steps={2, 4, 6}),
    Trait("Shapeshifter", steps={2, 4, 6}),
    Trait("Sugarcraft", steps={2, 4, 6}),
    Trait("Vanguard", steps={2, 4, 6}),
    Trait("Warrior", steps={2, 4, 6}),
    Trait("Witchcraft", steps={2, 4, 6, 8}),
    Trait("Explorer", steps={1}),
    Trait("Bat Queen", steps={1}),
    Trait("Best Friends", steps={1}),
    Trait("Ravenous", steps={1}),
    Trait("Druid", steps={1}),
    Trait("Preserver", steps={2, 3, 4, 5}),
    Trait("Chrono", steps={2, 4, 6}),
    ]


TRAIT_BREAKPOINTS_DICT = {trait.name: trait for trait in TRAIT_BREAKPOINTS}