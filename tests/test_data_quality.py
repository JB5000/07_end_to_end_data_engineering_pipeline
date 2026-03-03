import pytest

from src.data_quality import summarize_quality


def test_summarize_quality_happy_path() -> None:
    metrics = summarize_quality(total_rows=1000, invalid_rows=25, duplicate_rows=15)
    assert metrics["valid_rows"] == 960.0
    assert metrics["quality_score"] == 96.0


def test_summarize_quality_invalid_bounds() -> None:
    with pytest.raises(ValueError):
        summarize_quality(total_rows=10, invalid_rows=8, duplicate_rows=5)
