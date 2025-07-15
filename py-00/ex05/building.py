import sys as s


def analyze_string(user_input: str) -> dict:
    """
    Analyze character composition of a string.

    Counts and categorizes different types of characters in the input string,
    including uppercase letters, lowercase letters, digits, spaces, and
    punctuation marks.

    Args:
        user_input (str): The string to analyze.

    Returns:
        dict: A dictionary containing counts for each character type:
            - 'characters': Total character count
            - 'uppercase': Number of uppercase letters
            - 'lowercase': Number of lowercase letters
            - 'punctuation': Number of punctuation marks
            - 'spaces': Number of whitespace characters
            - 'digits': Number of digit characters
    """
    characters = 0
    spaces = 0
    lowers = 0
    uppers = 0
    digits = 0
    punctuation = 0

    for letter in user_input:
        characters += 1
        if letter.isspace():
            spaces += 1
        elif letter.islower():
            lowers += 1
        elif letter.isupper():
            uppers += 1
        elif letter.isdigit():
            digits += 1
        else:
            punctuation += 1
    result = {"characters": characters,
              "spaces": spaces,
              "lowercase": lowers,
              "uppercase": uppers,
              "digits": digits,
              "punctuation": punctuation}
    return result


def main():
    """
    Main entry point for the text analysis program.

    Takes text input via command line argument or prompts user for input,
    then analyzes and displays character type counts.

    Returns:
        None
    """
    if len(s.argv) == 1:
        user_text = input("What is the text to count?\n")
        data_result = analyze_string(user_text)
    elif len(s.argv) == 2:
        data_result = analyze_string(s.argv[1])
    else:
        print("AssertionError: more than one argument is provided")
        return

    print(f"The text contains {data_result['characters']} characters:")
    print(f"{data_result['uppercase']} upper letters")
    print(f"{data_result['lowercase']} lower letters")
    print(f"{data_result['punctuation']} punctuation marks")
    print(f"{data_result['spaces']} spaces")
    print(f"{data_result['digits']} digits")


if __name__ == "__main__":
    main()
