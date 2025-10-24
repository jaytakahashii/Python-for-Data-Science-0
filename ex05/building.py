import sys


def ispunctuation(char: str) -> bool:
    # check if a character is a punctuation mark
    if char in '''!()-[]{};:'"\\,<>./?@#$%^&*_~''':
        return True
    return False


def countChars(text: str) -> dict:
    # count types of characters in a string
    details = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }
    for char in text:
        if char.isupper():
            details["upper"] += 1
        elif char.islower():
            details["lower"] += 1
        elif ispunctuation(char):
            details["punctuation"] += 1
        elif char.isdigit():
            details["digits"] += 1
        elif char.isspace():
            details["spaces"] += 1
    return details


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            print("What is the text to count?")
            text: str = sys.stdin.read()
        else:
            text: str = sys.argv[1]
        counts: dict = countChars(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
