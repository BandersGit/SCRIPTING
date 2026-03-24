# import argparse

# parser = argparse.ArgumentParser(
#     description="Vi tar in två tal och räknar med dem", epilog="Text längst ner"
# )

# parser.add_argument(
#     "number1", type=float, help="Detta är ett heltal som ska skickas in"
# )
# parser.add_argument(
#     "number2", type=float, help="Detta är ett heltal som ska skickas in"
# )
# parser.add_argument("-v", "--verbose", action="store_true")
# parser.add_argument("-o", "--optional")

# args = parser.parse_args()

# if args.optional:
#     print(f"You provided the optional value: {args.optional}")

# if args.verbose:
#     print(f"Addition: {args.number1 + args.number2}")

#     print(f"Subtraction: {args.number1 - args.number2}")

#     print(f"Multiplication: {args.number1 * args.number2}")

#     print(f"Division: {args.number1 / args.number2}")
# else:
#     print(
#         f"{args.number1 + args.number2}, {args.number1 - args.number2}, {args.number1 * args.number2}, {args.number1 / args.number2}"
#     )

import argparse
# skapa ett ArgumentParser-objekt
parser = argparse.ArgumentParser(
    description="Detta är en beskrivning av mitt verktyg. Vi tar ett namn och skriver ut en hälsning i terminalen.",
    epilog="Detta är text som syns längst ner.",
)
"""
Allt här kommer bli argument vi skickar in
"""
# parser.add_argument("name", help="Detta är en textsträng som ska skickas in.")  # name blir namnet på variabeln i parsern
# här kommer ni att lägga alla era argument som behövs
# alltså first integer/float och second integer/float
# Positional arguments läggs i ordning
parser.add_argument("first", type=float)
parser.add_argument("second", type=float)

parser.add_argument("-o", "--optional")
# add_mutually_exclusive_group() blir som en if/elif
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-v", "--verbose", action="store_true"
)  # detta är en optional flag, store_true = False som default
group.add_argument(
    "-q", "--quiet", action="store_true"
)  # detta är en optional flag, store_true = False som default
args = parser.parse_args()
# Detta går men det finns ett bättre sätt i argparse
# args.first = float(args.first) # int() eller float() omvandlar bool()
# args.second = float(args.second)
if args.optional:  # optional är en sträng? Inte bool?
    print(f"You provided the optional value: {args.optional}")
if args.verbose:
    # långa variant av utskrift
    # verbose = en flagga
    print(50 * "*")
    print(f"Summan är: {args.first + args.second}!")
    print(f"Differensen är: {args.first - args.second}!")
    print(f"Produkten är: {args.first * args.second}!")
    print(f"Kvoten är: {args.first / args.second}!")
    print(50 * "*")
elif args.quiet:
    print(
        f"{args.first + args.second}, {args.first - args.second}, {args.first * args.second}, {args.first / args.second}"
    )
else:
    print("Last resort?")






