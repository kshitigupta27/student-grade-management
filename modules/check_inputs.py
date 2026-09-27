# input validation functions

def get_marks(subject_title):
    while True:
        try:
            m = float(input(f"Enter {subject_title} marks (0 to 100): "))
            if 0 <= m <= 100:
                return m
            print("Score has to be between 0 and 100. Try once more.")
        except ValueError:
            print("Not a valid number. Please type digits only.")

def get_reg_number():
    while True:
        r = input("Enter Registration No: ").strip().upper()
        if len(r) > 0:
            return r
        print("Registration number is required.")