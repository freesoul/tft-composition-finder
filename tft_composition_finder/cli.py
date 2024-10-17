from typing import List
import argparse
import dataclasses

from tft_composition_finder.schemas.emblems import Emblems
from tft_composition_finder.composers.bruteforce_composer import BruteforceComposer


@dataclasses.dataclass
class CliArgs:
    include_champs: str
    team_size: int
    emblems: List[Emblems]
    method: str


def get_cli_args() -> CliArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-champs", type=str)
    parser.add_argument("--team-size", type=int, default=8)
    parser.add_argument("--emblems", type=str)
    parser.add_argument("--method", type=str, default="bruteforce", choices=["bruteforce", "genetic"])
    args = parser.parse_args()

    if not args.include_champs:
        raise ValueError("You must provide at least one champion to include")

    if args.team_size < 1:
        raise ValueError("Team size must be at least 1")

    if args.method not in ["bruteforce", "genetic"]:
        raise ValueError("Method must be either 'bruteforce' or 'genetic'")

    if args.emblems:
        emblems = [Emblems.from_str(emblem_str) for emblem_str in args.emblems.split(",")]
    else:
        emblems = None

    return CliArgs(
        include_champs=args.include_champs,
        team_size=args.team_size,
        emblems=emblems,
        method=args.method,
    )


if __name__ == "__main__":

    args = get_cli_args()

    # composer = Composer(target_team_size=args.team_size, emblems=emblems)

    # if len(args.include_champs) > 0:
    #     champions = set()
    #     for champ_name in args.include_champs.split(","):
    #         champions.add(composer._get_champ(champ_name))
    #     start_comp = Composition(champions=champions, emblems=composer._emblems_dict)
    # else:
    #     start_comp = Composition(
    #         champions=set([champ for champ in TFT_CHAMPIONS if champ.name in INCLUDE_CHAMPS]),
    #         emblems=composer._emblems_dict,
    #     )

    # result = composer.compose(start_comp)

    # print("\nDone. Best compositions:")
    # for comp in composer._found_compositions:
    #     comp.pretty_print()
