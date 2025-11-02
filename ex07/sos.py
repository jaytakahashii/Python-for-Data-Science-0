import sys


def morse_encode(text):
    """
    Encodes a string into Morse Code using a dictionary.

    :param text: The string to encode.
    :return: The Morse Code string.
    :raises AssertionError: If the text contains unsupported characters.
    """
    MORSE_CODE = {
        " ": "/ ",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    encoded_message = []
    supported_chars = set(MORSE_CODE.keys())

    # Encoding loop
    for char in text.upper():
        # Check for unsupported characters
        if char not in supported_chars:
            raise AssertionError("the arguments are bad")

        morse_char = MORSE_CODE[char]

        if char != ' ':
            # Complete morse characters are separated by a single space
            morse_char += ' '

        encoded_message.append(morse_char)

    # Remove trailing spaces
    return "".join(encoded_message).strip()


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        input_string = sys.argv[1]
        morse_output = morse_encode(input_string)
        print(morse_output)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
