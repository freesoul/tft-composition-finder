
MIN_MAX_UNIT_BY_COST = {
    1: [0, 1],
    2: [0, 2],
    3: [1, 3],
    4: [1, 4],
    5: [0, 3],
}

MIN_DIFFERENT_TRAITS_PER_LEVEL = {
    2: 1,
    4: 2,
    6: 3,
    # 8: 4,
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
    "faerie_5": 0.7,
    "faerie_7": 1.2,
    "faerie_9": 4,

    "eldritch_3": 0.2,
    "eldritch_5": 0.5,
    "eldritch_7": 1.2,
    "eldritch_10": 4,

    "warrior_2": 0.3,
    "warrior_4": 1,
    "warrior_6": 2,

    "multistriker_3": 0.4,
    "multistriker_5": 0.7,
    "multistriker_7": 1.2,
    "multistriker_9": 3,

    "chrono_2": 0.4,
    "chrono_4": 0.8,
    "chrono_6": 1.9,

    "arcana_2": 0.2,
    "arcana_3": 0.4,
    "arcana_4": 1.2,
    "arcana_5": 1.8,

    "blaster_2": 0.4,
    "blaster_4": 1,
    "blaster_6": 1.8,

    "pyro_2": 0.3,
    "pyro_3": 0.5,
    "pyro_4": 1,
    "pyro_5": 1.8,

    "dragon_2": 0.4,
    "dragon_3": 1.6,

    "frost_3": 0.4,
    "frost_5": 1,
    "frost_7": 1.6,
    "frost_9": 4,

    "hunter_2": 0.5,
    "hunter_4": 0.8,
    "hunter_6": 2.2,

    "scholar_2": 0.5,
    "scholar_4": 1.3,
    "scholar_6": 2.2,

    "witchcraft_2": 0.5,
    "witchcraft_4": 0.8,
    "witchcraft_6": 1.5,
    "witchcraft_8": 3,

    "sugarcraft_2": 0.5,
    "sugarcraft_4": 1.2,
    "sugarcraft_6": 3,

    "shapeshifter_2": 0.5,
    "shapeshifter_4": 0.8,
    "shapeshifter_6": 1.5,
    "shapeshifter_8": 3,

    "mage_3": 0.6,
    "mage_5": 1.2,
    "mage_7": 1.8,
    "mage_10": 4,

    "portal_3": 0.4,
    "portal_6": 0.8,
    "portal_8": 1.8,
    "portal_10": 4,

    "vanguard_2": 0.5,
    "vanguard_4": 1.2,
    "vanguard_6": 2.5,

    "bastion_2": 0.5,
    "bastion_4": 0.2,
    "bastion_6": 1.8,
    "bastion_8": 3.5,

    "preserver_2": 0.5,
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

MIN_SCORE = 7

MIN_TRAIT_LEVEL = 4

UNIT_SCORE = {
    "Diana": 1,
    "Milio": 1,
    "Morgana": 1,
    "Rakan": 1,
    "Taric": 1,
    "Briar": 0.8,
    "Bard": 0.8,
    "Camille": 0.8,
    "Fiora": 0.8,
    "Gwen": 0.8,
    "Hecarim": 0.8,
    "Kalista": 0.8,
    "Karma": 0.8,
    "Mordekaiser": 0.8,
    "Nami": 0.8,
    "Nasus": 0.8,
    "Norra": 0.8,
    "Ryze": 0.8,
    "Shen": 0.8,
    "Smolder": 0.8,
    "Swain": 0.8,
    "Syndra": 0.8,
    "Tahm Kench": 0.8,
    "Varus": 0.8,
    "Xerath": 0.8,
    "Akali": 0.6,
    "Ashe": 0.6,
    "Cassiopeia": 0.6,
    "Elise": 0.6,
    "Galio": 0.6,
    "Hwei": 0.6,
    "Jinx": 0.6,
    "Kassadin": 0.6,
    "Neeko": 0.6,
    "Nilah": 0.6,
    "Olaf": 0.6,
    "Vex": 0.6,
    "Wukong": 0.6,
    "Ziggs": 0.6,
    "Zilean": 0.6,
    "Zoe": 0.6,
    "Blitzcrank": 0,
    "Ezreal": 0,
    "Jax": 0,
    "Jayce": 0,
    "Katarina": 0,
    "Kogmaw": 0,
    "Nomsy": 0,
    "Nunu": 0,
    "Poppy": 0,
    "Rumble": 0,
    "Shyvana": 0,
    "Tristana": 0,
    "Veigar": 0,
    "Ahri": -0.3,
    "Lillia": -0.3,
    "Seraphine": -0.3,
    "Soraka": -0.3,
    "Twitch": -0.3,
    "Warwick": -0.3,
}
