# tests/test_app.py
import unittest
from src.app import format_student_score

class TestStudentScore(unittest.TestCase):
    """Test Case 1: Valid passing score."""
    def test_passing_score(self):
        result = format_student_score("Alice", 85.5)
        self.assertEqual(result, "Student: Alice | Score: 85.50 | Status: PASSED")

    """Test Case 2: Valid failing score."""
    def test_failing_score(self):
        result = format_student_score("Bob", 65.0)
        self.assertEqual(result, "Student: Bob | Score: 65.00 | Status: FAILED")

    """Test Case 3: Edge case: Out-of-bounds score raises ValueError."""
    def test_invalid_score_exception(self):
        with self.assertRaises(ValueError):
            format_student_score("Charlie", 105.0)

if __name__ == '__main__':
    unittest.main()