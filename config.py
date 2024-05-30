MIN_TEAM_SIZE = 7
MAX_TEAM_SIZE = 8
MIN_MAX_UNIT_BY_COST = {
    1: [0, 1],
    2: [0, 2],
    3: [1, 3],
    4: [2, 4],
    5: [1, 3],
}
MIN_DIFFERENT_TRAITS_LVL2 = 0
MIN_DIFFERENT_TRAITS_LVL3 = 0
MIN_DIFFERENT_TRAITS_LVL6 = 3
MIN_DIFFERENT_TRAITS_LVL8 = 4

INCLUDE_CHAMPS = ["Syndra", "Illaoi", "Ahri"]
EXCLUDE_CHAMPS = ["Kobuko", "Jax", "Garen", "Sivir", "Kha'zix", "Malphite", "Cho'gath", "Yone", "Kayn", "Kai'sa"]

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
    "behemot_4": 0.7,
    "reaper_4": 0.7,
    "umbral_2": 0.7,
}

MAX_ATTEMPTS_PER_NUM_CHAMPS = {
    9: 3,
    8: 5,
    7: 7,
    6: 12,
    5: 25,
    4: 50,
    3: 100,
}

MIN_SCORE = 17

# MAX_ATTEMPTS_PER_NUM_CHAMPS = {
# }

# MIN_SCORE=18
