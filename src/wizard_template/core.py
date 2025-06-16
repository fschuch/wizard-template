"""Module containing the core functionality of the demo project."""


class NotAnIntegerError(TypeError):
    """Raised when the input is not an integer."""

    def __init__(self, incoming_type):
        """Initialize the error."""
        self.message = f"Input must be an integer, got {incoming_type}."
        super().__init__(self.message)


def demo_function(incoming_int: int) -> int:
    """Demo function that doubles the input.

    Args:
        incoming_int: The input to be doubled

    Returns:
       The doubled input

    Raises:
        NotAnIntegerError: If tried with an invalid input

    Examples:
        >>> demo_function(2)
        4
        >>> demo_function(3)
        6
    """
    if isinstance(incoming_int, int) is False:
        raise NotAnIntegerError(type(incoming_int))
    return incoming_int * 2
