"""Tests for {{MODULE_NAME}}.

This module contains tests for the {{MODULE_NAME}} module.
"""

import pytest

from {{PACKAGE_NAME}}.{{MODULE_NAME}} import {{CLASS_OR_FUNCTION_NAME}}


class Test{{ClassName}}:
    """Test suite for {{CLASS_OR_FUNCTION_NAME}}."""

    def test_{{test_name}}_basic(self) -> None:
        """Test basic functionality."""
        # Arrange
        {{ARRANGE_CODE}}

        # Act
        result = {{ACT_CODE}}

        # Assert
        assert result == {{EXPECTED_VALUE}}

    def test_{{test_name}}_edge_case(self) -> None:
        """Test edge case handling."""
        # Test implementation
        pass

    def test_{{test_name}}_raises_exception(self) -> None:
        """Test that invalid input raises appropriate exception."""
        with pytest.raises({{EXCEPTION_TYPE}}, match="{{ERROR_MESSAGE}}"):
            {{CODE_THAT_RAISES}}

    @pytest.mark.parametrize(
        ("input_value", "expected"),
        [
            ({{INPUT_1}}, {{EXPECTED_1}}),
            ({{INPUT_2}}, {{EXPECTED_2}}),
            ({{INPUT_3}}, {{EXPECTED_3}}),
        ],
    )
    def test_{{test_name}}_parametrized(
        self, input_value: {{INPUT_TYPE}}, expected: {{EXPECTED_TYPE}}
    ) -> None:
        """Test with multiple inputs using parametrize."""
        result = {{FUNCTION_CALL}}(input_value)
        assert result == expected

    @pytest.fixture
    def {{fixture_name}}(self) -> {{FIXTURE_TYPE}}:
        """Fixture providing {{FIXTURE_DESCRIPTION}}."""
        return {{FIXTURE_VALUE}}

    def test_with_fixture(self, {{fixture_name}}: {{FIXTURE_TYPE}}) -> None:
        """Test using fixture."""
        result = {{FUNCTION_CALL}}({{fixture_name}})
        assert result is not None
