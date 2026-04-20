"""
Validation helpers for API input values.
"""

from fastapi import HTTPException


def validate_utf8_text(value: str, field_name: str) -> None:
    """Validate that a text input can be safely represented as UTF-8."""
    try:
        value.encode("utf-8", "strict")
    except UnicodeEncodeError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid encoding in {field_name}. Please use UTF-8 text."
        ) from None
