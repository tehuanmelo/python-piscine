
def check_list_type(lst: list[int | float]) -> bool:
    """
    Checks if the values of a list only have integers
    or floats

    Return:
    True if all the values are either int or float
    Raises a TypeError if not
    """
    if not len(lst):
        raise ValueError("The list cant be empty")
    if not isinstance(lst, list):
        raise TypeError("Argument passed is not a List")
    for value in lst:
        if not isinstance(value, (int, float)):
            raise TypeError("Lists must contains either floats or integers")
    return True


def check_lists_length(lst_1: list[int | float],
                       lst_2: list[int | float]) -> bool:
    """
    Checks the length of two lists

    Return:
    True if the lengths are the same
    False if is not
    """
    if not len(lst_1) or not len(lst_2):
        raise ValueError("The lists cant be empty")
    if len(lst_1) != len(lst_2):
        raise ValueError("The length of the lists must be "
                         "the same")
    return True


def check_limit_type(limit):
    """Check if the value passed is an integer"""
    if not isinstance(limit, int):
        raise ValueError("The limit value must be an integer")


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    give_bmi take 2 lists of integers or floats in
    input and returns a list of BMI values.
    """
    try:
        check_lists_length(height, weight)
        check_list_type(height)
        check_list_type(weight)
        return [w / h ** 2 for h, w in zip(height, weight)]
    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    apply_limit, accepts a list of integers or floats and an
    integer representing a limit as parameters. It returns a
    list of booleans (True if above the limit).
    """
    try:
        check_list_type(bmi)
        check_limit_type(limit)
        limits = [value > limit for value in bmi]
        return limits
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    """Entry point of the program"""
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
