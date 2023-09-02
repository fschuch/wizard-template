"""Module containing the core functionality of the demo project."""


def demo_function(incoming_int: int) -> int:
    """Demo function that doubles the input.

    Args
    ----
    incoming_int: The input to be doubled.

    Returns
    -------
    The doubled input.

    Raises
    ------
    TypeError: If the input is not an integer.

    Examples
    --------
    >>> demo_function(2)
    4
    >>> demo_function(3)
    6
    """
    if isinstance(incoming_int, int) is False:
        raise TypeError(f"Input must be an integer, got {type(incoming_int)}.")
    return incoming_int * 2
