# validating user inputs here
def get_marks(sub):
    while True:
        try:
            m = float(input("Enter marks for " + sub + ": "))
            if m >= 0 and m <= 100:
                return m
            else:
                print("Marks must be between 0 and 100!")
        except:
            print("Please enter numbers only.")

def get_reg_number():
    while True:
        r = input("Enter Registration No: ")
        r = r.strip()
        if len(r) > 0:
            return r
        else:
            print("Registration number cannot be empty!")
