import sys
from ft_filter import ft_filter


def main():
    """
    Entry point of the program.
    """
    arguments = sys.argv
    try:
        if len(arguments) != 3:
            raise Exception()
        string = str(arguments[1])
        length = int(arguments[2])
        words = [word for word in string.split() if len(word) >= length]
        print(ft_filter(lambda item: len(item) >= length, words))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
