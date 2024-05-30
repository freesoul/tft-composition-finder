MIN_TEAM_SIZE = 7
MAX_TEAM_SIZE = 8
MIN_MAX_UNIT_BY_COST = {
    1: [0, 1],
    2: [0, 2],
    3: [1, 3],
    4: [2, 4],
    5: [1, 3],
}

MIN_DIFFERENT_TRAITS_PER_LEVEL = {
    2: 1,
    4: 2,
    6: 3,
    8: 4,
}

INCLUDE_CHAMPS = [("Ahri", "Caitlyn", "Kog'maw"), ("Diana", "Illaoi"), ("Syndra", "Ornn", "Lee Sin"), ("Hwei", "Sett")]
EXCLUDE_CHAMPS = []

INCLUDE_TRAITS = []

KEEP_N_BEST = 10

TRAIT_SCORE_WEIGHT = {
    "ghostly_8": 1.2,
    "porcelain_6": 1.2,
    "sniper_6": 1.2,
    "altruist_4": 1.2,
    "heavenly_7": 1.2,
    "dryad_6": 1.2,
    "warden_6": 1.2,
    "exalted_3": 1.2,
    "altruist_3": 1.2,
    "fated_3": 1.2,
    "heavenly_3": 1.2,
    "dragonlord_5": 1.2,
    "great_1": 1.2,
    "fated_7": 1.2,
    "sage_4": 1.2,
    "umbral_4": 0.7,
    "storyweaver_5": 0.7,
    "duelist_4": 0.7,
    "heavenly_5": 0.7,
    "fortune_3": 0.7,
    "fortune_5": 0.7,
    "trickshot_2": 0.7,
    "sniper_2": 0.7,
    "fortune_7": 0.7,
    "bruiser_6": 0.7,
    "fated_5": 0.7,
    "arcanist_6": 0.7,
    "reaper_4": 0.7,
    "umbral_2": 0.7,
    "arcanist_4": 0.5,
    "behemoth_4": 0.5,
}

# This starts from the non-fixed num champs
MAX_ATTEMPTS = [999, 25, 12, 10, 7, 5, 3, 2, 2, 1]

MIN_SCORE = 7


MIN_TRAIT_LEVEL = 4

UNIT_SCORE = {
    "Sett": 1,
    "Ahri": 0.5,
    "Caitlyn": 0.5,
    "Kog'maw": 0.5,
    "Rakan": 1,
    "Udyr": 1,
    "Wukong": 1,
    "Hwei": 1,
    "Xayah": 1,
    "Lissandra": 1,
    "Riven": -1,
    "Rek'sai": -1,
    "Kobuko": -0.5,
    "Jax": -1,
    "Garen": -1,
    "Sivir": -1,
    "Kha'zix": -1,
    "Malphite": -1,
    "Cho'gath": -1,
    "Yone": -1,
    "Kayn": -1.5,
    "Kai'sa": -1,
    "Teemo": -1,
    "Lux": -1,
    "Bard": -1.5,
    "Tristana": -1,
    "Soraka": 0.5,
    "Syndra": 0.5,
}
