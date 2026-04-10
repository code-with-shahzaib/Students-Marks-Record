import json
import os

DATA_FILE = "students.json"
student_data = {}


# ==============================
# File Handling
# ==============================

def load_data():
    """Load data from JSON file safely."""
    global student_data

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                student_data = json.load(file)
        except (json.JSONDecodeError, IOError):
            print("⚠️ Corrupted file. Starting fresh.")
            student_data = {}
    else:
        student_data = {}


def save_data():
    """Save data to JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(student_data, file, indent=4)
    except IOError:
        print("❌ Error saving data.")


# ==============================
# Input System
# ==============================

def get_valid_number(prompt, min_val=None, max_val=None):
    """Reusable numeric validator."""
    while True:
        try:
            value = float(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a number.")


def take_input():
    """Take dynamic number of students from user."""
    global student_data

    count = int(get_valid_number("Enter number of students: ", 1))

    for i in range(1, count + 1):
        while True:
            name = input(f"\nEnter name of student {i}: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            if name in student_data:
                print("Student already exists. Use a different name.")
                continue

            marks = get_valid_number(f"Enter {name}'s marks (0-100): ", 0, 100)

            student_data[name] = marks
            break

    save_data()
    print("✅ Data added successfully.")


# ==============================
# Core Features
# ==============================

def display_data():
    """Display all student records."""
    if not student_data:
        print("⚠️ No data available.")
        return

    print("\n--- Student Records ---")
    for i, (name, marks) in enumerate(student_data.items(), 1):
        print(f"{i}. {name} → {marks} Marks")


def highest_scorer():
    """Get highest scorer."""
    if not student_data:
        print("No data available.")
        return

    name = max(student_data, key=student_data.get)
    print(f"🏆 Highest Scorer: {name} ({student_data[name]})")


def lowest_scorer():
    """Get lowest scorer."""
    if not student_data:
        print("No data available.")
        return

    name = min(student_data, key=student_data.get)
    print(f"📉 Lowest Scorer: {name} ({student_data[name]})")


def average_marks():
    """Calculate average."""
    if not student_data:
        print("No data available.")
        return

    avg = sum(student_data.values()) / len(student_data)
    print(f"📊 Average Marks: {avg:.2f}")


def declare_result():
    """Separate pass and fail students."""
    pass_students = {}
    fail_students = {}

    for name, marks in student_data.items():
        if marks >= 50:
            pass_students[name] = marks
        else:
            fail_students[name] = marks

    return pass_students, fail_students


def display_results():
    """Display pass/fail lists."""
    if not student_data:
        print("No data available.")
        return

    pass_students, fail_students = declare_result()

    print("\n--- Pass Students ---")
    for i, (name, marks) in enumerate(pass_students.items(), 1):
        print(f"{i}. {name} → {marks}")

    print("\n--- Fail Students ---")
    for i, (name, marks) in enumerate(fail_students.items(), 1):
        print(f"{i}. {name} → {marks}")


def pass_fail_percentage():
    """Calculate pass/fail percentage."""
    if not student_data:
        print("No data available.")
        return

    pass_students, fail_students = declare_result()
    total = len(student_data)

    print(f"Pass: {(len(pass_students)/total)*100:.2f}%")
    print(f"Fail: {(len(fail_students)/total)*100:.2f}%")


# ==============================
# Extra Control Features
# ==============================

def delete_student():
    """Delete a student record."""
    if not student_data:
        print("No data available.")
        return

    name = input("Enter student name to delete: ").strip()

    if name in student_data:
        del student_data[name]
        save_data()
        print("🗑️ Student removed.")
    else:
        print("Student not found.")


def update_student():
    """Update existing student's marks."""
    if not student_data:
        print("No data available.")
        return

    name = input("Enter student name to update: ").strip()

    if name in student_data:
        new_marks = get_valid_number("Enter new marks (0-100): ", 0, 100)
        student_data[name] = new_marks
        save_data()
        print("✏️ Record updated.")
    else:
        print("Student not found.")


def clear_all_data():
    """Clear entire database."""
    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":
        student_data.clear()
        save_data()
        print("🔥 All data cleared.")
    else:
        print("Operation cancelled.")


# ==============================
# Menu System
# ==============================

def main_menu():
    print("\n===== Student Marks Manager =====")
    print("1. Add Students")
    print("2. Show Data")
    print("3. Highest Scorer")
    print("4. Lowest Scorer")
    print("5. Average Marks")
    print("6. Display Results")
    print("7. Pass/Fail Percentage")
    print("8. Update Student")
    print("9. Delete Student")
    print("10. Clear All Data")
    print("11. Exit")


# ==============================
# Entry Point
# ==============================

if __name__ == "__main__":

    load_data()
    print("=" * 10, "Student Manager", "=" * 10)

    while True:
        main_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            take_input()
        elif choice == "2":
            display_data()
        elif choice == "3":
            highest_scorer()
        elif choice == "4":
            lowest_scorer()
        elif choice == "5":
            average_marks()
        elif choice == "6":
            display_results()
        elif choice == "7":
            pass_fail_percentage()
        elif choice == "8":
            update_student()
        elif choice == "9":
            delete_student()
        elif choice == "10":
            clear_all_data()
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")