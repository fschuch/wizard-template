"""Test the core module."""
import pytest

from wizard_template.core import demo_function


@pytest.mark.parametrize(
    "incoming_int, expected_result", [(2, 4), (3, 6), (5, 10)]
)
def test_demo_function__success(incoming_int, expected_result):
    """Test the demo function returns the expected value."""
    actual_result = demo_function(incoming_int)
    assert actual_result == expected_result


@pytest.mark.parametrize("incoming_int", ["string", 1.0, None])
def test_demo_function__failure(incoming_int):
    """Test the demo function raises TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        demo_function(incoming_int)
