import sys


def morse(char) -> str:
    """
    Converts a single character into its Morse code equivalent.

    Parameters:
    char (str): A single alphanumeric character or space.

    Returns:
    str: The Morse code string for the given character,
    ending with a space.

    Raises:
    Exception: If the character is not found in the Morse dictionary.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }
    if char in NESTED_MORSE:
        return NESTED_MORSE[char]
    else:
        raise Exception()


def sos(input) -> str:
    """
    Converts an input string to its Morse code representation.

    Parameters:
    input (str): The string to convert to Morse code.

    Returns:
    str: The Morse code equivalent of the input string.
    """
    morse_str = ""
    for char in input:
        morse_str += morse(char)
    return morse_str


def main():
    """
    Entry point of the program.

    Validates the arguments provided via the command line.
    If valid, it converts the input string to Morse code
    using the sos() function.

    Raises:
    Exception: If the number of arguments is not exactly 1
    """
    arguments = sys.argv
    try:
        if len(arguments) != 2:
            raise Exception()
        arg_str = str(arguments[1])
        print(sos(arg_str))
    except Exception:
        print('AssertionError: the arguments are bad')


if __name__ == "__main__":
    main()
