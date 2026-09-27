from modules.file_handler import read_data, write_data
from modules.grade_calc import find_grade
from modules.check_inputs import get_marks, get_reg_number

def add_student():
    records = read_data()
    reg = get_reg_number()

    for s in records:
        if s["RegNo"] == reg:
            print("Record with this Registration No already exists!")
            return

    name = input("Enter Student Name: ").strip()
    m1 = get_marks("Subject 1")
    m2 = get_marks("Subject 2")
    m3 = get_marks("Subject 3")

    avg = round((m1 + m2 + m3) / 3, 2)
    grade = find_grade(avg)

    new_entry = {
        "RegNo": reg,
        "Name": name,
        "Mark1": m1,
        "Mark2": m2,
        "Mark3": m3,
        "Average": avg,
        "Grade": grade
    }

    records.append(new_entry)
    write_data(records)
    print(f"\nStudent {name} added successfully with Grade {grade}!")

def view_all_students():
    records = read_data()
    if not records:
        print("\nNo student records found.")
        return

    print("\n" + "-" * 75)
    print(f"{'Reg No':<12}{'Name':<20}{'M1':<8}{'M2':<8}{'M3':<8}{'Avg':<10}{'Grade':<6}")
    print("-" * 75)
    for s in records:
        print(f"{s['RegNo']:<12}{s['Name']:<20}{s['Mark1']:<8}{s['Mark2']:<8}{s['Mark3']:<8}{s['Average']:<10.2f}{s['Grade']:<6}")
    print("-" * 75)

def search_student():
    records = read_data()
    reg = input("Enter Registration No to search: ").strip().upper()

    for s in records:
        if s["RegNo"] == reg:
            print("\n--- Student Found ---")
            print(f"Reg No  : {s['RegNo']}")
            print(f"Name    : {s['Name']}")
            print(f"Marks   : {s['Mark1']}, {s['Mark2']}, {s['Mark3']}")
            print(f"Average : {s['Average']}%")
            print(f"Grade   : {s['Grade']}")
            return
    print("\nNo student found with that registration number.")

def delete_student():
    records = read_data()
    reg = input("Enter Registration No to delete: ").strip().upper()

    updated = [s for s in records if s["RegNo"] != reg]
    if len(updated) == len(records):
        print("\nRecord not found.")
    else:
        write_data(updated)
        print(f"\nRecord for {reg} deleted successfully.")