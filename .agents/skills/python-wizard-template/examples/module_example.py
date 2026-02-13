"""Example module following wizard-template conventions.

This module demonstrates the coding standards and patterns expected in
projects created from the wizard-template.
"""

from typing import Any


def process_data(data: list[Any], *, filter_empty: bool = True) -> list[Any]:
    """Process a list of data items.

    This function demonstrates proper docstring format, type hints,
    and keyword-only arguments.

    Args:
        data: List of items to process.
        filter_empty: Whether to filter out empty items.

    Returns:
        Processed list of items.

    Raises:
        ValueError: If data is None.

    Examples:
        >>> process_data([1, 2, 3])
        [1, 2, 3]
        >>> process_data([1, "", 3], filter_empty=True)
        [1, 3]
        >>> process_data([1, "", 3], filter_empty=False)
        [1, '', 3]
    """
    if data is None:
        raise ValueError("data cannot be None")

    if filter_empty:
        return [item for item in data if item]
    return data


class DataProcessor:
    """A class for processing data with state.

    This class demonstrates proper class documentation and initialization.

    Attributes:
        multiplier: Factor to multiply processed values.
        strict_mode: Whether to raise errors on invalid data.

    Examples:
        >>> processor = DataProcessor(multiplier=2.0)
        >>> processor.process(5)
        10.0
    """

    def __init__(self, multiplier: float = 1.0, *, strict_mode: bool = False) -> None:
        """Initialize the DataProcessor.

        Args:
            multiplier: Factor to multiply processed values.
            strict_mode: Whether to raise errors on invalid data.
        """
        self.multiplier = multiplier
        self.strict_mode = strict_mode

    def process(self, value: int | float) -> float:
        """Process a single value.

        Args:
            value: The value to process.

        Returns:
            The processed value.

        Raises:
            ValueError: If value is negative and strict_mode is True.
        """
        if self.strict_mode and value < 0:
            raise ValueError("Negative values not allowed in strict mode")
        return float(value) * self.multiplier
