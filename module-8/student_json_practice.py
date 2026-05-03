"""
Sam Dirr
May 3rd, 2026
Module 8 JSON Practice assignment

This program loads a class list from Student.json, displays the original
students, adds one new student record, displays the updated list, and writes
the updated class list back to the JSON file.
"""

import json
from pathlib import Path


JSON_FILE = Path(__file__).with_name("Student.json")


def print_students(class_list):
    """Print every student record in the required assignment format."""
    for student in class_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , Email = {student['Email']}"
        )


def main():
    """Load, update, display, and save the student list."""
    with JSON_FILE.open("r", encoding="utf-8") as file:
        class_list = json.load(file)

    print("This is the original Student list.")
    print_students(class_list)

    new_student = {
        "F_Name": "Samuel",
        "L_Name": "Dirr",
        "Student_ID": 21420947,
        "Email": "sdirr@my365.bellevue.edu",
    }

    if new_student not in class_list:
        class_list.append(new_student)

    print()
    print("This is the updated Student list.")
    print_students(class_list)

    with JSON_FILE.open("w", encoding="utf-8") as file:
        json.dump(class_list, file, indent=4)

    print()
    print("The Student.json file was updated.")


if __name__ == "__main__":
    main()
