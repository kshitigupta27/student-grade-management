# reading and writing to csv file
import csv

def load_data(filename):
    # return list of rows from csv
    rows = []
    try:
        f = open(filename, "r")
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
        f.close()
    except:
        return []
    return rows

def save_data(filename, rows):
    # write records back to csv file
    if len(rows) == 0:
        return
    
    f = open(filename, "w", newline="")
    headers = ["RegNo", "Name", "Subject1", "Subject2", "Subject3", "Average", "Grade"]
    writer = csv.DictWriter(f, fieldnames=headers)
    
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    f.close()

