import sys
from ft_filter import ft_filter


def error():
    """Prints an error message"""
    print("AssertionError: the arguments are bad")
    exit()


def ft_split(s):
    """Split text by spaces"""
    words = []
    current = ""
    if s:
        for c in s:
            if c in " \t\n\r\0":
                if current:
                    words.append(current)
                    current = ""
            else:
                current += c
        if current:
            words.append(current)
    return words


def main():
    """
    The program accepts two arguments:
    a string(S), and an integer(N).
    The program returns a list of words from S
    that have a length greater than N.
    """
    if len(sys.argv) != 3:
        error()
        exit()
    try:
        input_str = sys.argv[1]
        input_int = int(sys.argv[2])
        print(ft_filter(lambda s: len(s) >= input_int, ft_split(input_str)))
    except ValueError:
        error()


if __name__ == "__main__":
    main()
