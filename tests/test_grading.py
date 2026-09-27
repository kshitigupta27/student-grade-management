# simple checks for grading calculation
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.grade_calc import find_grade

def test_grade_boundaries():
    # checking border marks
    assert find_grade(95) == 'S'
    assert find_grade(85) == 'A'
    assert find_grade(75) == 'B'
    assert find_grade(65) == 'C'
    assert find_grade(50) == 'D'
    assert find_grade(42) == 'F'
    print("Grade checks passed successfully!")

if __name__ == "__main__":
    test_grade_boundaries()