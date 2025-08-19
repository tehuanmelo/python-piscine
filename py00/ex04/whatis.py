import sys


def main(argv):
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if (len(argv) == 2):
            assert argv[1].isnumeric() \
                or argv[1][0] == "-" and argv[1][1:].isnumeric(), \
                "argument is not integer"
            print("I'm Even.") if int(argv[1]) % 2 == 0 else print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
