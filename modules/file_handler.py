import csv
import os

CSV_PATH = "student_records.csv"
FIELDS = ["RegNo", "Name", "Mark1", "Mark2", "Mark3", "Average", "Grade"]

def read_data():
    student_list = []
    if not os.path.exists(CSV_PATH):
        return student_list

    with open(CSV_PATH, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_list.append({
                "RegNo": row["RegNo"],
                "Name": row["Name"],
                "Mark1": float(row["Mark1"]),
                "Mark2": float(row["Mark2"]),
                "Mark3": float(row["Mark3"]),
                "Average": float(row["Average"]),
                "Grade": row["Grade"]
            })
    return student_list

def write_data(student_list):
    with open(CSV_PATH, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for item in student_list:
            writer.writerow(item)