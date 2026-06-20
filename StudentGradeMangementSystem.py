"""
Dictionary - key + value pair
left side = key
right side = value
{key: value, key: value, key: value}


1. Add
2. Update
3. Delete
4. View
5. Exit/Stop


Basics 

Create a dictionary
var = {"name": "Veriel", "name": "Luna", "name": "Zeke"}
print(var)  

Accessing an element
print(var["name"])  

Updating an element
var["name"] = "Zeke"
print(var)

Deleting an element
del var["name"]
print(var)

View
print(var)  

"""


# Initializing an empty dictionary to store student_grades

student_grades = {}

# Adding a new student 

def add_student(name, grade):
    student_grades[name] = grade
    print(f"{name} with grade {grade} has been added successfully!")

# Update a student's grade

def update_student(name, new_grade):
    if name in student_grades:
        student_grades[name] = new_grade
        print(f"{name} grade has been updated to {new_grade} successfully!")
    else:
        print(f"{name} not found")

# Delete a student name

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted successfully!")
    else:
        print(f"{name} not found")

# View all students

def display_all_students():
    if student_grades:
        print("Student Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = int(input("Enter your choice = "))

        if choice == 1:
            name = input("Enter your name = ")
            grade = int(input("Enter your grade = "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter your name = ")
            grade = int(input("Enter your grade = "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter your name = ")
            delete_student(name)

        elif choice == 4:
            display_all_students(name)

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")

main()

            



           


