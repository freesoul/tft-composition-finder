
MIN_MAX_UNIT_BY_COST = {
    # 1: [0, 2],
    # 2: [0, 2],
    # 3: [1, 3],
    # 4: [1, 4],
    # 5: [0, 3],
}

MIN_DIFFERENT_TRAITS_PER_LEVEL = {
}

INCLUDE_CHAMPS = []
EXCLUDE_CHAMPS = []

INCLUDE_TRAITS = []

KEEP_N_BEST = 10

TRAIT_SCORE_WEIGHT = {

    "incantor_2": 0.2,
    "incantor_4": 0.4,

    "honeymancy_3": 0.3,
    "honeymancy_5": 0.6,
    "honeymancy_7": 1,

    "faerie_3": 0.5,
    "faerie_5": 2,
    "faerie_7": 10,
    "faerie_9": 6,

    "eldritch_3": 0.1,
    "eldritch_5": 0.5,
    "eldritch_7": 1.2,
    "eldritch_10": 4,

    "warrior_2": 0.3,
    "warrior_4": 1,
    "warrior_6": 2,

    "multistriker_3": 0.2,
    "multistriker_5": 0.5,
    "multistriker_7": 1.2,
    "multistriker_9": 3,

    "chrono_2": 0.2,
    "chrono_4": 0.8,
    "chrono_6": 1.9,

    "arcana_2": 0.1,
    "arcana_3": 0.4,
    "arcana_4": 1.2,
    "arcana_5": 1.8,

    "blaster_2": 0.2,
    "blaster_4": 1,
    "blaster_6": 1.8,

    "pyro_2": 0.1,
    "pyro_3": 0.5,
    "pyro_4": 1,
    "pyro_5": 1.8,

    "dragon_2": 0.4,
    "dragon_3": 1.6,

    "frost_3": 0.2,
    "frost_5": 1,
    "frost_7": 1.6,
    "frost_9": 4,

    "hunter_2": 0.3,
    "hunter_4": 0.8,
    "hunter_6": 2.2,

    "scholar_2": 0.1,
    "scholar_4": 1.3,
    "scholar_6": 2.2,

    "witchcraft_2": 0.2,
    "witchcraft_4": 0.8,
    "witchcraft_6": 1.5,
    "witchcraft_8": 3,

    "sugarcraft_2": 0.6,
    "sugarcraft_4": 1.2,
    "sugarcraft_6": 3,

    "shapeshifter_2": 0.2,
    "shapeshifter_4": 0.8,
    "shapeshifter_6": 1.5,
    "shapeshifter_8": 3,

    "mage_3": 0.6,
    "mage_5": 1.2,
    "mage_7": 1.8,
    "mage_10": 4,

    "portal_3": 0.1,
    "portal_6": 0.8,
    "portal_8": 1.8,
    "portal_10": 4,

    "vanguard_2": 0.2,
    "vanguard_4": 1.2,
    "vanguard_6": 2.5,

    "bastion_2": 0.2,
    "bastion_4": 0.2,
    "bastion_6": 1.8,
    "bastion_8": 3.5,

    "preserver_2": 0.2,
    "preserver_3": 0.7,
    "preserver_4": 1.2,
    "preserver_5": 2,

    # These are taken into account by the champ boost itself
    "best_friends_1": 0,
    "ravenous_1": 0,
    "ascendant_1": 0,
    "bat_queen_1": 0,
}

# This starts from the non-fixed num champs
MAX_ATTEMPTS = [999, 200, 100, 50, 25, 15, 10, 7, 5, 2]

MIN_SCORE = 0.0

MIN_TRAIT_LEVEL = 2

UNIT_SCORE = {
    "Karma": 0.08,
    "Mordekaiser": 0.08,
    "Nami": 0.08,
    "Nasus": 0.08,
    "Norra": 0.08,
    "Ryze": 0.08,
    "Shen": 0.08,
    "Smolder": 0.08,
    "Swain": 0.08,
    "Syndra": 0.08,
    "Tahm Kench": 0.08,
    "Varus": 0.08,
    "Xerath": 0.08,
    "Akali": 0.06,
    "Ashe": 0.06,
    "Cassiopeia": 0.06,
    "Elise": 0.06,
    "Galio": 0.06,
    "Hwei": 0.06,
    "Jinx": 0.06,
    "Kassadin": 0.06,
    "Neeko": 0.06,
    "Nilah": 0.06,
    "Olaf": 0.06,
    "Vex": 0.06,
    "Wukong": 0.06,
    "Ziggs": 0.06,
    "Zilean": 0.06,
    "Zoe": 0.06,
    "Blitzcrank": 0.0,
    "Ezreal": 0.0,
    "Jax": 0.0,
    "Jayce": 0.0,
    "Katarina": 0.0,
    "Kogmaw": 0.0,
    "Nomsy": 0.0,
    "Nunu": 0.0,
    "Poppy": 0.0,
    "Rumble": 0.0,
    "Shyvana": 0.0,
    "Tristana": 0.0,
    "Veigar": 0.0,
    "Ahri": -0.03,
    "Lillia": -0.03,
    "Seraphine": -0.03,
    "Soraka": -0.03,
    "Twitch": -0.03,
    "Warwick": -0.03
}


SINERGIES = [
    ("pyro", "multistriker", 1),
    ("faerie", "mage", -2), # Not tanky enough
    ("faerie", "pyro", -2), # Not tanky enough
]

