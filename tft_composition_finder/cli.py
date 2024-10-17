
# if __name__ == "__main__":

#     import argparse

#     parser = argparse.ArgumentParser()
#     parser.add_argument("--include-champs", type=str)
#     parser.add_argument("--team-size", type=int, default=8)
#     parser.add_argument("--emblems", type=str)
#     args = parser.parse_args()

#     if args.emblems:
#         emblems = [
#             Emblems.from_str(emblem_str) for emblem_str in args.emblems.split(",")
#         ]
#     else:
#         emblems = []

#     composer = Composer(target_team_size=args.team_size, emblems=emblems)

#     if len(args.include_champs) > 0:
#         champions = set()
#         for champ_name in args.include_champs.split(","):
#             champions.add(composer._get_champ(champ_name))
#         start_comp = Composition(champions=champions, emblems=composer._emblems_dict)
#     else:
#         start_comp = Composition(
#             champions=set(
#                 [champ for champ in TFT_CHAMPIONS if champ.name in INCLUDE_CHAMPS]
#             ),
#             emblems=composer._emblems_dict,
#         )

#     result = composer.compose(start_comp)

#     print("\nDone. Best compositions:")
#     for comp in composer._found_compositions:
#         comp.pretty_print()
