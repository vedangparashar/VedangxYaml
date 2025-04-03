import yaml

def load_data(file_path):
    """Load data from a YAML file."""
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def save_data(file_path, data):
    """Save updated data back to the YAML file."""
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def display_students(students):
    """Display all students."""
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")

def filter_students_by_gpa(students, min_gpa):
    """Filter and display students with a GPA above the specified minimum."""
    filtered_students = [s for s in students if s['gpa'] >= min_gpa]
    print(f"\nStudents with GPA >= {min_gpa}:")
    if filtered_students:
        for student in filtered_students:
            print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}, GPA: {student['gpa']}")
    else:
        print("No students found.")

def sort_students(students, order="asc"):
    """Sort students by GPA in ascending or descending order."""
    return sorted(students, key=lambda x: x['gpa'], reverse=(order == "desc"))

def update_student(students):
    """Update a student's information."""
    name = input("\nEnter the name of the student to update: ").strip()
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Current details: {student}")
            student['age'] = int(input("Enter new age: "))
            student['major'] = input("Enter new major: ").strip()
            student['gpa'] = float(input("Enter new GPA: "))
            print("Student information updated successfully!")
            return True
    print("Student not found!")
    return False

def main():
    file_path = 'students.yaml'
    
    # Load the data from YAML
    data = load_data(file_path)
    students = data['students']

    while True:
        print("\nOptions:")
        print("1. Display all students")
        print("2. Filter students by GPA")
        print("3. Sort students by GPA")
        print("4. Update student information")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            display_students(students)
        elif choice == "2":
            min_gpa = float(input("\nEnter minimum GPA to filter students: "))
            filter_students_by_gpa(students, min_gpa)
        elif choice == "3":
            order = input("Enter sort order (asc/desc): ").strip().lower()
            students = sort_students(students, order)
            display_students(students)
        elif choice == "4":
            if update_student(students):
                save_data(file_path, {'students': students})
        elif choice == "5":
            save_data(file_path, {'students': students})
            print("Changes saved. Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()