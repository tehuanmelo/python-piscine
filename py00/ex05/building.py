import sys


def parse(user_input: str) -> tuple:
    """
    Parses the text and counts:
   - Total number of characters
   - Uppercase letters
   - Lowercase letters
   - Punctuation marks
   - Spaces
   - Digits
   """
    characters = len(user_input)
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
    return characters, uppers, lowers, punctuations, spaces, digits


def building(data: tuple) -> str:
    """
    Builds the string with all the statistics in a clear format.
    """
    characters, uppers, lowers, punctuations, spaces, digits = data
    result = f"The text contains {characters} characters:\n"
    result += f"{uppers} upper letters\n"
    result += f"{lowers} lower letters\n"
    result += f"{punctuations} punctuation marks\n"
    result += f"{spaces} spaces\n"
    result += f"{digits} digits"
    return result


def main():
    """
    Entry point of the program. Handles input and error checking.
    Calls the building() function to analyze the text.
    Prints the output
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        user_input = ""
        if len(sys.argv) < 2:
            print('What is the text to count?')
            user_input = sys.stdin.readline()
            if user_input == "":
                raise EOFError
        else:
            user_input = sys.argv[1]
        print(building(parse(user_input)))

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except KeyboardInterrupt:
        print("\n^C pressed. Exiting gracefully.")
        exit(1)
    except EOFError:
        print("\nNo input received (EOF). Exiting.")
        exit(1)


if __name__ == "__main__":
    main()
