import sys


def building(user_input: str):
    """
    Analyzes a given text and counts character types.
    Prints:
    - Total number of characters
    - Number of uppercase letters
    - Number of lowercase letters
    - Number of punctuation marks
    - Number of spaces
    - Number of digits
    """
    uppers = 0
    lowers = 0
    punctuations = 0
    spaces = 0
    digits = 0
    for letter in user_input:
        if letter.isupper():
            uppers += 1
        elif letter.islower():
            lowers += 1
        elif letter.isspace():
            spaces += 1
        elif letter.isdigit():
            digits += 1
        else:
            punctuations += 1

    print(f"The text contains {len(user_input)} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Entry point of the program. Handles input and error checking.
    Calls the building() function to analyze the text.
    """
    try:
        user_input = ""
        if len(sys.argv) < 2:
            print('What is the text to count?')
            user_input = sys.stdin.read()
        elif len(sys.argv) > 2:
            print('AssertionError: more than one argument is provided')
            return
        else:
            user_input = sys.argv[1]

        building(user_input)

    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
