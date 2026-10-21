# Student Score Manager
# Collection types: List, Dictionary, and Set

students = []
student_names = set()


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if name.casefold() in student_names:
        print("This student already exists.")
        return

    try:
        math_score = float(input("Enter Mathematics score (0-100): "))
        english_score = float(input("Enter English score (0-100): "))
        python_score = float(input("Enter Python score (0-100): "))

        scores = [math_score, english_score, python_score]

        if any(score < 0 or score > 100 for score in scores):
            print("Scores must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numbers for the scores.")
        return

    average = sum(scores) / len(scores)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

    students.append(student)
    student_names.add(name.casefold())

    print("Student record added successfully!")


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- STUDENT RESULTS ---")

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Scores: {student['scores']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Grade: {student['grade']}")
        print("-" * 25)


def search_student():
    name = input("Enter student name to search: ").strip()

    for student in students:
        if student["name"].casefold() == name.casefold():
            print("\nStudent found!")
            print(f"Name: {student['name']}")
            print(f"Scores: {student['scores']}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT SCORE MANAGER =====")
        print("1. Add Student")
        print("2. View All Results")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the Student Score Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
