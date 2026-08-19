students = {}

while True:
    print("\n===== ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = []
        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P" or status == "A":
                students[name].append(status)
                print("Attendance marked successfully!")
            else:
                print("Please enter only P or A.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\n===== ATTENDANCE REPORT =====")

        for name, attendance in students.items():
            total = len(attendance)
            present = attendance.count("P")

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print("\nStudent:", name)
            print("Attendance:", attendance)
            print("Percentage:", percentage, "%")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")