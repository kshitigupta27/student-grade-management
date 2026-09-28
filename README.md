# Student Grade Management System

A modular terminal-based Python application for managing student academic records.

## Project Structure
- `main.py`: Entry point for the CLI menu.
- `modules/check_inputs.py`: Input validations for marks and registration numbers.
- `modules/file_handler.py`: CSV read and write operations.
- `modules/grade_calc.py`: Average calculation and letter grade evaluation.
- `modules/student_records.py`: Student record management logic.
- `tests/test_grading.py`: Automated assertion unit tests.
- `student_records.csv`: Persistent record storage.

## How to Run
1. Open the project folder in terminal.
2. Run the main application:
python main.py

3. Run automated unit tests:
python -m unittest tests/test_grading.py