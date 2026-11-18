# College Admission Management System

students = []

def add_student():
    print("\n--- Enter Student Admission Details ---")

    student = {}

    student["Name"] = input("Enter Student Name: ")
    student["Application Number"] = input("Enter Application Number: ")
    student["Date of Birth"] = input("Enter Date of Birth: ")
    student["Gender"] = input("Enter Gender: ")
    student["Contact Number"] = input("Enter Contact Number: ")
    student["Email ID"] = input("Enter Email ID: ")
    student["Address"] = input("Enter Address: ")
    student["10th Marks"] = input("Enter 10th Marks: ")
    student["12th Marks"] = input("Enter 12th Marks: ")
    student["Previous College"] = input("Enter Previous College Name: ")
    student["Selected Course"] = input("Enter Selected Course: ")
    student["Admission Status"] = input("Enter Admission Status: ")

    students.append(student)

    print("\nAdmission Details Added Successfully!")

def display_students():
    if not students:
        print("\nNo Admission Records Found!")
    else:
        print("\n--- COLLEGE ADMISSION DETAILS ---")

        for student in students:
            for key, value in student.items():
                print(key, ":", value)
            print("--------------------------------")

def search_student():
    number = input("Enter Application Number: ")

    for student in students:
        if student["Application Number"] == number:
            print("\nStudent Record Found!")
            for key, value in student.items():
                print(key, ":", value)
            return

    print("\nStudent Record Not Found!")

while True:
    print("\n===== COLLEGE ADMISSION MANAGEMENT SYSTEM =====")
    print("1. Add Admission Details")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice! Try Again.")