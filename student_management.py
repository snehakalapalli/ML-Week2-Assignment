import csv
import os

FILENAME = "students.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Name", "Marks"])

def add_student():
    roll_no = input("Enter Roll Number: ").strip()
    if search_student_by_roll(roll_no, quiet=True):
        print(f"Error: Roll Number {roll_no} already exists!\n")
        return

    name = input("Enter Name: ").strip()
    marks = input("Enter Marks: ").strip()

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, marks])
    print("Student added successfully!\n")

def search_student_by_roll(roll_no, quiet=False):
    found = False
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if row and row[0] == roll_no:
                if not quiet:
                    print("\n--- Student Details ---")
                    print(f"Roll Number : {row[0]}")
                    print(f"Name        : {row[1]}")
                    print(f"Marks       : {row[2]}\n")
                return True
    if not quiet and not found:
        print("Student not found!\n")
    return False

def delete_student():
    roll_no = input("Enter Roll Number to delete: ").strip()
    students = []
    found = False

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        for row in reader:
            if row:
                if row[0] == roll_no:
                    found = True
                else:
                    students.append(row)

    if found:
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])
            writer.writerows(students)
        print("Student record deleted successfully!\n")
    else:
        print("Roll Number not found!\n")

def display_all():
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        rows = list(reader)

        if not rows:
            print("No student records found.\n")
            return

        print("\n--- All Students ---")
        print(f"{'Roll No':<10} {'Name':<20} {'Marks':<10}")
        print("-" * 40)
        for row in rows:
            if row:
                print(f"{row[0]:<10} {row[1]:<20} {row[2]:<10}")
        print()

def main():
    while True:
        print("===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            roll = input("Enter Roll Number to search: ").strip()
            search_student_by_roll(roll)
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
                  
