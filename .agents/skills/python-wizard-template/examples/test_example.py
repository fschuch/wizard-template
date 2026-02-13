"""Example test file following wizard-template conventions.

This module demonstrates testing patterns expected in projects created
from the wizard-template.
"""

import pytest

from my_package.module_example import DataProcessor, process_data


class TestProcessData:
    """Test suite for process_data function."""

    def test_process_data_basic(self) -> None:
        """Test basic data processing."""
        result = process_data([1, 2, 3])
        assert result == [1, 2, 3]

    def test_process_data_filter_empty(self) -> None:
        """Test filtering empty items."""
        result = process_data([1, "", None, 3], filter_empty=True)
        assert result == [1, 3]

    def test_process_data_no_filter(self) -> None:
        """Test without filtering."""
        result = process_data([1, "", 3], filter_empty=False)
        assert result == [1, "", 3]

    def test_process_data_none_raises(self) -> None:
        """Test that None input raises ValueError."""
        with pytest.raises(ValueError, match="cannot be None"):
            process_data(None)

    @pytest.mark.parametrize(
        ("input_data", "expected"),
        [
            ([1, 2, 3], [1, 2, 3]),
            ([1, "", 3], [1, 3]),
            ([], []),
        ],
    )
    def test_process_data_parametrized(
        self, input_data: list, expected: list
    ) -> None:
        """Test process_data with various inputs using parametrize."""
        result = process_data(input_data, filter_empty=True)
        assert result == expected


class TestDataProcessor:
    """Test suite for DataProcessor class."""

    def test_init_defaults(self) -> None:
        """Test initialization with default values."""
        processor = DataProcessor()
        assert processor.multiplier == 1.0
        assert processor.strict_mode is False

    def test_init_custom(self) -> None:
        """Test initialization with custom values."""
        processor = DataProcessor(multiplier=2.5, strict_mode=True)
        assert processor.multiplier == 2.5
        assert processor.strict_mode is True

    def test_process_basic(self) -> None:
        """Test basic value processing."""
        processor = DataProcessor(multiplier=2.0)
        result = processor.process(5)
        assert result == 10.0

    def test_process_negative_strict(self) -> None:
        """Test that negative values raise error in strict mode."""
        processor = DataProcessor(strict_mode=True)
        with pytest.raises(ValueError, match="Negative values not allowed"):
            processor.process(-5)

    def test_process_negative_non_strict(self) -> None:
        """Test that negative values work in non-strict mode."""
        processor = DataProcessor(multiplier=2.0, strict_mode=False)
        result = processor.process(-5)
        assert result == -10.0

    @pytest.fixture
    def processor(self) -> DataProcessor:
        """Fixture providing a DataProcessor instance."""
        return DataProcessor(multiplier=3.0)

    def test_with_fixture(self, processor: DataProcessor) -> None:
        """Test using fixture."""
        result = processor.process(4)
        assert result == 12.0
