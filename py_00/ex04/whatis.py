import sys


def main():
    try:
        if len(sys.argv) < 2:
            return
        elif len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
            return
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
