# Logic for grade evaluation and batch summary

# functions for average and grading
def find_average(m1, m2, m3):
    # simple 3 subject average
    total = m1 + m2 + m3
    avg = total / 3
    return round(avg, 2)

def find_grade(avg):
    # grade mapping based on percentage
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "F"
