def ft_filter(fun, iter):
    """
    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    """
    if fun:
        return [item for item in iter if fun(item)]
    else:
        return [item for item in iter if item]
