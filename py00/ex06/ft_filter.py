def ft_filter(fun, iter) -> list:
    """
    filter(function or None, iterable) --> list

    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    """
    try:
        if fun is None:
            return [item for item in iter if item]
        else:
            return [item for item in iter if fun(item)]
    except Exception:
        print("Error: error filtering the iterable")


def main():
    """
    Entry point of the program.
    """
    pass


if __name__ == "__main__":
    main()
