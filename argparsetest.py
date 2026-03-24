import argparse

parser = argparse.ArgumentParser(
    description="Vi tar ett namn och skriver en hälsning", epilog="Text längst ner"
)

parser.add_argument("name", help="Detta är en textsträng som ska skickas in")

args = parser.parse_args()

print(f"Hello {args.name}!")
