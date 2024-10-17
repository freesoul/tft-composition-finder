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
        emblems = []

    return CliArgs(
        include_champs=args.include_champs,
        team_size=args.team_size,
        emblems=emblems,
        method=args.method,
    )


if __name__ == "__main__":

    args = get_cli_args()

    if args.method == "bruteforce":
        composer = BruteforceComposer(args.team_size, args.emblems)
    elif args.method == "genetic":
        raise NotImplementedError("Genetic method not implemented yet")
    else:
        raise ValueError("Invalid method")
    
    for composition in composer.compose():
        composition.pretty_print()
