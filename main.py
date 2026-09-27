# Main Entry Point for Student Grade Management System

from modules.student_records import (
    add_student,
    view_all_students,
    search_student,
    delete_student
)
from modules.grade_calc import display_summary
from modules.file_handler import read_data

def show_menu():
    print("\n" + "=" * 45)
    print("   STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add New Student Record")
    print("2. Display All Student Records")
    print("3. Search Student by Reg No")
    print("4. Remove Student Record")
    print("5. View Class Analytics & Summary")
    print("6. Exit")
    print("=" * 45)

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            students = read_data()
            display_summary(students)
        elif choice == '6':
            print("\nExiting program. All data is saved.")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 6.")

if __name__ == "__main__":
    main()
    