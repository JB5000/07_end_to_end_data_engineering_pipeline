"""Data quality metrics for ingestion and transformation stages."""


def summarize_quality(total_rows: int, invalid_rows: int, duplicate_rows: int) -> dict[str, float]:
    if total_rows < 0 or invalid_rows < 0 or duplicate_rows < 0:
        raise ValueError("row counts must be non-negative")
    if invalid_rows + duplicate_rows > total_rows:
        raise ValueError("invalid_rows + duplicate_rows cannot exceed total_rows")

    valid_rows = total_rows - invalid_rows - duplicate_rows
    quality_score = round((valid_rows / total_rows) * 100, 2) if total_rows else 0.0
    return {
        "total_rows": float(total_rows),
        "valid_rows": float(valid_rows),
        "invalid_rows": float(invalid_rows),
        "duplicate_rows": float(duplicate_rows),
        "quality_score": quality_score,
    }
