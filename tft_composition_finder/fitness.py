from tft_composition_finder.schemas.composition import Composition
from tft_composition_finder.sets import (
    TRAIT_SCORE_WEIGHT,
    UNIT_SCORE,
    INCLUDE_TRAITS,
    MIN_MAX_UNIT_BY_COST,
    MIN_SCORE,
    MIN_TRAIT_LEVEL,
)


def _has_required_traits(composition: Composition) -> bool:
    for req_trait in INCLUDE_TRAITS:
        if not composition.includes_trait(req_trait):
            return False
    return True


def _has_n_costs_in_range(composition: Composition) -> bool:
    for cost, min_max in MIN_MAX_UNIT_BY_COST.items():
        num_champs_n_cost = composition.get_num_champs_n_cost(cost)
        if num_champs_n_cost < min_max[0] or num_champs_n_cost > min_max[1]:
            return False
    return True


def _get_traits_score(composition: Composition) -> float:
    score = 0.0
    for trait, breakpoint_num in composition.traits_with_breakpoints.items():
        trait_key = f"{trait}_{breakpoint_num}"
        try:
            score += TRAIT_SCORE_WEIGHT[trait_key] * breakpoint_num
        except KeyError:
            score += breakpoint_num
    return score


def _get_units_score(composition: Composition) -> float:
    score = 0.0
    for champ in composition.champions:
        if champ.name in UNIT_SCORE:
            score += UNIT_SCORE[champ.name]
    return score


def fitness(
    composition: Composition,
) -> float:
    """
    Determines the fitness of a composition. A higher fitness score indicates a better composition.
    """

    if not _has_required_traits(composition):
        return 0.0

    if not _has_n_costs_in_range(composition):
        return 0.0

    if composition.max_trait_level < MIN_TRAIT_LEVEL:
        return 0.0

    score = _get_traits_score(composition) + _get_units_score(composition)

    if score < MIN_SCORE:
        return 0.0

    return score
