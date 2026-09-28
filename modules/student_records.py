# main logic for adding, searching, deleting students
from modules.file_handler import load_data, save_data
from modules.check_inputs import get_marks, get_reg_number
from modules.grade_calc import find_average, find_grade

FILE = "student_records.csv"

def add_student():
    # add new student if reg no not already present
    records = load_data(FILE)
    reg = get_reg_number()

    for s in records:
        if s["RegNo"] == reg:
            print("Student already exists with this registration number!")
            return

    name = input("Enter Student Name: ").strip()
    m1 = get_marks("Subject 1")
    m2 = get_marks("Subject 2")
    m3 = get_marks("Subject 3")

    avg = find_average(m1, m2, m3)
    grade = find_grade(avg)

    new_student = {
        "RegNo": reg,
        "Name": name,
        "Subject1": str(m1),
        "Subject2": str(m2),
        "Subject3": str(m3),
        "Average": str(avg),
        "Grade": grade
    }

    records.append(new_student)
    save_data(FILE, records)
    print("Student added successfully!")

def show_all():
    # display all saved records
    records = load_data(FILE)
    if len(records) == 0:
        print("No student records found.")
        return

    print("\n--- Student List ---")
    for s in records:
        print("Reg No:", s["RegNo"], "| Name:", s["Name"], "| Average:", s["Average"], "| Grade:", s["Grade"])

def search_student():
    # find student by reg no
    records = load_data(FILE)
    reg = input("Enter Reg No to search: ").strip()

    for s in records:
        if s["RegNo"] == reg:
            print("\nStudent Found:")
            print("Reg No:", s["RegNo"])
            print("Name:", s["Name"])
            print("Marks:", s["Subject1"], s["Subject2"], s["Subject3"])
            print("Average:", s["Average"])
            print("Grade:", s["Grade"])
            return

    print("Student not found!")

def delete_student():
    # remove student from csv
    records = load_data(FILE)
    reg = input("Enter Reg No to delete: ").strip()
    found = False

    new_records = []
    for s in records:
        if s["RegNo"] == reg:
            found = True
        else:
            new_records.append(s)

    if found:
        save_data(FILE, new_records)
        print("Record deleted successfully.")
    else:
        print("Record not found, nothing deleted.")
