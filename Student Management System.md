# Student Management System 📝
![student-management-system](https://github.com/zahariev-webbersof/python-fundamentals-05-2024/assets/68993494/746ccfd8-f414-4714-96f9-e9d704cce587)

The goal of this project is to create a simple student management system using Python. This system will allow users to add, update, delete, and search for student records. Each student record will include information such as name, age, grade, and subjects. 
This project will give students practical experience with strings, integers, floats, booleans, lists, dictionaries, sets, and tuples.

## ✅ Project Requirements

- Data Types and Variables

- Understand and use different data types including strings, integers, floats, booleans, lists, dictionaries, sets, and tuples.
Tasks to Implement

- Add Student:
Create a function to add a new student record. Each record should include the student's name (string), age (int), grade (float), and subjects (list of strings).
- Update Student:
Create a function to update an existing student record. Allow updating of any of the fields (name, age, grade, subjects).
- Delete Student:
Create a function to delete a student record based on the student's name.
- Search Student:
Create a function to search for a student by name and return their record.
- List All Students:
Create a function to list all student records.

## ✅ Documentation and Comments

Include comments explaining each function and its purpose.
Provide documentation strings for each function, describing the parameters and return values.
User Interaction

Create a main program that prompts the user to choose which task they want to perform.
Use input prompts to gather the necessary data from the user.
Display the results of the chosen task in a clear and user-friendly manner.

### Now, let's write the code for this project:
[![My Skills](https://skillicons.dev/icons?i=python,windows,apple,linux&theme=light)](https://skillicons.dev)
```python

# Dictionary to store student records
students = {}

def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    # Code to add a new student record

def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """
    # Check if the student exists
    # Prompt the user to update fields and keep current values if fields are empty
    # Code to update the student's record

def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    # Check if the student exists
    # Code to delete the student's record

def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    # Check if the student exists
    # Code to return the student's record

def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students

def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")
        
        # Prompt user for their choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

```

## ✅ Additional Notes for Students
- Comments: Follow the comments and implement the necessary logic in each function.
- Error Handling: Add error handling where appropriate, such as checking for the existence of a student record before attempting to update or delete it.
- User Interaction: Ensure that user prompts and outputs are clear and user-friendly.
- Data Validation: Validate inputs where necessary (e.g., ensure age is an integer, grade is a float, etc.).


This skeleton provides the structure and necessary functions for the student management system. Your task is to complete the implementation by writing the code for each function according to the provided comments and requirements.
