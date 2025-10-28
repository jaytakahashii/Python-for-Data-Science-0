def ft_filter(function_to_apply: callable, iterable) -> object:
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    return [element for element in iterable if function_to_apply(element)]
