import sys as s

if len(s.argv) == 1:
    pass
elif len(s.argv) == 2:
    try:
        num = int(s.argv[1])
        abs_num = abs(num)
        if abs_num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
else:
    print("AssertionError: more than one argument is provided")
