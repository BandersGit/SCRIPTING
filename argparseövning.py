import argparse

parser = argparse.ArgumentParser(
    description="Vi tar in två tal och räknar med dem", epilog="Text längst ner"
)

parser.add_argument(
    "number1", type=float, help="Detta är ett heltal som ska skickas in"
)
parser.add_argument(
    "number2", type=float, help="Detta är ett heltal som ska skickas in"
)
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-o", "--optional")

args = parser.parse_args()

if args.optional:
    print(f"You provided the optional value: {args.optional}")

if args.verbose:
    print(f"Addition: {args.number1 + args.number2}")

    print(f"Subtraction: {args.number1 - args.number2}")

    print(f"Multiplication: {args.number1 * args.number2}")

    print(f"Division: {args.number1 / args.number2}")
else:
    print(
        f"{args.number1 + args.number2}, {args.number1 - args.number2}, {args.number1 * args.number2}, {args.number1 / args.number2}"
    )
