# src/app.py

def format_student_score(name: str, score: float) -> str:
    """Formats student laboratory score and evaluates passing status."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    status = "PASSED" if score >= 70.0 else "FAILED"
    return f"Student: {name} | Score: {score:.2f} | Status: {status}"