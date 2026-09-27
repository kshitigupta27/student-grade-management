# Logic for grade evaluation and batch summary

def find_grade(avg_val):
    if avg_val >= 90:
        return 'S'
    elif avg_val >= 80:
        return 'A'
    elif avg_val >= 70:
        return 'B'
    elif avg_val >= 60:
        return 'C'
    elif avg_val >= 50:
        return 'D'
    else:
        return 'F'

def display_summary(students):
    if not students:
        print("\nNo entries available for analytics.")
        return

    averages = [s["Average"] for s in students]
    total = len(students)
    batch_mean = sum(averages) / total

    print("\n" + "=" * 40)
    print("      CLASS ANALYTICS REPORT")
    print("=" * 40)
    print(f"Total Student Count : {total}")
    print(f"Batch Mean Average  : {batch_mean:.2f}%")
    print(f"Top Score           : {max(averages):.2f}%")
    print(f"Lowest Score        : {min(averages):.2f}%")
    print("-" * 40)
    print("Grade Distribution:")
    for g in ['S', 'A', 'B', 'C', 'D', 'F']:
        cnt = sum(1 for s in students if s["Grade"] == g)
        print(f"  Grade {g} -> {cnt} student(s)")
    print("=" * 40)