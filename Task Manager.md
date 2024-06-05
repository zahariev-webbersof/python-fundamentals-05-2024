#  Task Manager System 📝🔰

![1SvzKctRCi8bwB0QPdOZkBP0pRhsOqZpl0wjs6y0](https://github.com/zahariev-webbersof/python-fundamentals-05-2024/assets/68993494/0142e16c-2b6a-4c0b-89d4-82110845a9a7)

## ✅ Project Overview

The objective of this project is to develop a suite of Python functions for a basic task manager application and provide a user menu to interact with these functions. You will create 20 functions that handle various tasks such as creating, updating, deleting, and managing tasks, as well as generating reports and performing searches.

## ✅ Project Requirements

- Functionality: Implement 20 distinct functions related to task management.
- Documentation: Each function should include a docstring explaining what it does, its parameters, and its return value.
- Error Handling: Functions should include appropriate error handling to manage invalid inputs or other potential issues.
- User Menu: Provide a user menu to interact with the functions and see their functionality in action.
- Code Quality: Code should follow PEP 8 guidelines and be well-organized and readable.

# Additional Information

## ✅Suggested Functions

### Task Creation and Management:

- add_task(tasks, task): Adds a new task to the task list.
- remove_task(tasks, task_id): Removes a task by its ID.
- update_task(tasks, task_id, updated_task): Updates an existing task.
- get_task(tasks, task_id): Retrieves a task by its ID.

### Task Attributes Management:

- set_task_priority(tasks, task_id, priority): Sets the priority of a task.
- set_task_deadline(tasks, task_id, deadline): Sets the deadline for a task.
- mark_task_as_completed(tasks, task_id): Marks a task as completed.
- set_task_description(tasks, task_id, description): Sets the description for a task.

### Task Search and Filtering:

- search_tasks_by_keyword(tasks, keyword): Searches tasks by a keyword in the description.
- filter_tasks_by_priority(tasks, priority): Filters tasks by priority.
- filter_tasks_by_status(tasks, status): Filters tasks by their completion status.
- filter_tasks_by_deadline(tasks, deadline): Filters tasks by their deadline.

### Task Statistics and Reports:

- count_tasks(tasks): Returns the total number of tasks.
- count_completed_tasks(tasks): Returns the number of completed tasks.
- count_pending_tasks(tasks): Returns the number of pending tasks.
- generate_task_summary(tasks): Generates a summary report of all tasks.

### Miscellaneous:

- save_tasks_to_file(tasks, file_path): Saves the task list to a file.
- load_tasks_from_file(file_path): Loads the task list from a file.
- sort_tasks_by_deadline(tasks): Sorts tasks by their deadline.
- sort_tasks_by_priority(tasks): Sorts tasks by their priority.

## Tech stack:
[![My Skills](https://skillicons.dev/icons?i=python,windows,apple,linux&theme=light)](https://skillicons.dev)

## Python Code Skeleton with User Menu
Below is a skeleton code to get you started:

```python
import json
from datetime import datetime


def add_task(tasks, task):
    """
    Adds a new task to the task list.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task (dict): The task to be added.

    Returns:
    list of dict: Updated list of tasks.
    """


def remove_task(tasks, task_id):
    """
    Removes a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be removed.

    Returns:
    list of dict: Updated list of tasks.
    """


def update_task(tasks, task_id, updated_task):
    """
    Updates an existing task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    updated_task (dict): The updated task details.

    Returns:
    list of dict: Updated list of tasks.
    """


def get_task(tasks, task_id):
    """
    Retrieves a task by its ID.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be retrieved.

    Returns:
    dict: The task with the specified ID, or None if not found.
    """


def set_task_priority(tasks, task_id, priority):
    """
    Sets the priority of a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    priority (str): The new priority level.

    Returns:
    list of dict: Updated list of tasks.
    """


def set_task_deadline(tasks, task_id, deadline):
    """
    Sets the deadline for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    deadline (str): The new deadline.

    Returns:
    list of dict: Updated list of tasks.
    """


def mark_task_as_completed(tasks, task_id):
    """
    Marks a task as completed.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be marked as completed.

    Returns:
    list of dict: Updated list of tasks.
    """


def set_task_description(tasks, task_id, description):
    """
    Sets the description for a task.

    Parameters:
    tasks (list of dict): The current list of tasks.
    task_id (int): The ID of the task to be updated.
    description (str): The new description.

    Returns:
    list of dict: Updated list of tasks.
    """


def search_tasks_by_keyword(tasks, keyword):
    """
    Searches tasks by a keyword in the description.

    Parameters:
    tasks (list of dict): The current list of tasks.
    keyword (str): The keyword to search for.

    Returns:
    list of dict: Tasks that contain the keyword in their description.
    """


def filter_tasks_by_priority(tasks, priority):
    """
    Filters tasks by priority.

    Parameters:
    tasks (list of dict): The current list of tasks.
    priority (str): The priority level to filter by.

    Returns:
    list of dict: Tasks with the specified priority.
    """


def filter_tasks_by_status(tasks, status):
    """
    Filters tasks by their completion status.

    Parameters:
    tasks (list of dict): The current list of tasks.
    status (bool): The completion status to filter by.

    Returns:
    list of dict: Tasks with the specified completion status.
    """


def filter_tasks_by_deadline(tasks, deadline):
    """
    Filters tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.
    deadline (str): The deadline to filter by.

    Returns:
    list of dict: Tasks with the specified deadline.
    """


def count_tasks(tasks):
    """
    Returns the total number of tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The total number of tasks.
    """


def count_completed_tasks(tasks):
    """
    Returns the number of completed tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of completed tasks.
    """


def count_pending_tasks(tasks):
    """
    Returns the number of pending tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    int: The number of pending tasks.
    """


def generate_task_summary(tasks):
    """
    Generates a summary report of all tasks.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    dict: A summary report containing total, completed, and pending tasks.
    """


def save_tasks_to_file(tasks, file_path):
    """
    Saves the task list to a file.

    Parameters:
    tasks (list of dict): The current list of tasks.
    file_path (str): The path to the file where tasks will be saved.

    Returns:
    None
    """


def load_tasks_from_file(file_path):
    """
    Loads the task list from a file.

    Parameters:
    file_path (str): The path to the file where tasks are saved.

    Returns:
    list of dict: The loaded list of tasks.
    """


def sort_tasks_by_deadline(tasks):
    """
    Sorts tasks by their deadline.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """


def sort_tasks_by_priority(tasks):
    """
    Sorts tasks by their priority.

    Parameters:
    tasks (list of dict): The current list of tasks.

    Returns:
    list of dict: The sorted list of tasks.
    """


def print_menu():
    """
    Prints the user menu.
    """
    menu = """
    Task Manager Menu:
    1. Add Task
    2. Remove Task
    3. Update Task
    4. Get Task
    5. Set Task Priority
    6. Set Task Deadline
    7. Mark Task as Completed
    8. Set Task Description
    9. Search Tasks by Keyword
    10. Filter Tasks by Priority
    11. Filter Tasks by Status
    12. Filter Tasks by Deadline
    13. Count Tasks
    14. Count Completed Tasks
    15. Count Pending Tasks
    16. Generate Task Summary
    17. Save Tasks to File
    18. Load Tasks from File
    19. Sort Tasks by Deadline
    20. Sort Tasks by Priority
    21. Exit
    """
    print(menu)


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = {
                'id': int(input("Enter task ID: ")),
                'description': input("Enter task description: "),
                'priority': input("Enter task priority (low, medium, high): "),
                'deadline': input("Enter task deadline (YYYY-MM-DD): "),
                'completed': False
            }
            tasks = add_task(tasks, task)
            print("Task added successfully.")
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            tasks = remove_task(tasks, task_id)
            print("Task removed successfully.")
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            updated_task = {
                'description': input("Enter new task description: "),
                'priority': input("Enter new task priority (low, medium, high): "),
                'deadline': input("Enter new task deadline (YYYY-MM-DD): ")
            }
            tasks = update_task(tasks, task_id, updated_task)
            print("Task updated successfully.")
        elif choice == '4':
            task_id = int(input("Enter task ID to get: "))
            task = get_task(tasks, task_id)
            print("Task details:", task)
        elif choice == '5':
            task_id = int(input("Enter task ID to set priority: "))
            priority = input("Enter new priority (low, medium, high): ")
            tasks = set_task_priority(tasks, task_id, priority)
            print("Task priority set successfully.")
        elif choice == '6':
            task_id = int(input("Enter task ID to set deadline: "))
            deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks = set_task_deadline(tasks, task_id, deadline)
            print("Task deadline set successfully.")
        elif choice == '7':
            task_id = int(input("Enter task ID to mark as completed: "))
            tasks = mark_task_as_completed(tasks, task_id)
            print("Task marked as completed.")
        elif choice == '8':
            task_id = int(input("Enter task ID to set description: "))
            description = input("Enter new description: ")
            tasks = set_task_description(tasks, task_id, description)
            print("Task description set successfully.")
        elif choice == '9':
            keyword = input("Enter keyword to search: ")
            found_tasks = search_tasks_by_keyword(tasks, keyword)
            print("Tasks found:", found_tasks)
        elif choice == '10':
            priority = input("Enter priority to filter by (low, medium, high): ")
            filtered_tasks = filter_tasks_by_priority(tasks, priority)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '11':
            status = input("Enter status to filter by (completed/pending): ").lower() == 'completed'
            filtered_tasks = filter_tasks_by_status(tasks, status)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '12':
            deadline = input("Enter deadline to filter by (YYYY-MM-DD): ")
            filtered_tasks = filter_tasks_by_deadline(tasks, deadline)
            print("Filtered tasks:", filtered_tasks)
        elif choice == '13':
            total_tasks = count_tasks(tasks)
            print("Total number of tasks:", total_tasks)
        elif choice == '14':
            completed_tasks = count_completed_tasks(tasks)
            print("Number of completed tasks:", completed_tasks)
        elif choice == '15':
            pending_tasks = count_pending_tasks(tasks)
            print("Number of pending tasks:", pending_tasks)
        elif choice == '16':
            summary = generate_task_summary(tasks)
            print("Task Summary:", summary)
        elif choice == '17':
            file_path = input("Enter file path to save tasks: ")
            save_tasks_to_file(tasks, file_path)
            print("Tasks saved to file.")
        elif choice == '18':
            file_path = input("Enter file path to load tasks from: ")
            tasks = load_tasks_from_file(file_path)
            print("Tasks loaded from file.")
        elif choice == '19':
            tasks = sort_tasks_by_deadline(tasks)
            print("Tasks sorted by deadline.")
        elif choice == '20':
            tasks = sort_tasks_by_priority(tasks)
            print("Tasks sorted by priority.")
        elif choice == '21':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


```

## ✳️ Evaluation Criteria ✳️
- Correctness: Functions produce correct results for various inputs.
- Completeness: All 20 functions are implemented and integrated with the user menu.
- Documentation: Code is well-documented with clear and concise docstrings.
- Error Handling: Functions handle errors gracefully.
- Code Quality: Code is clean, readable, and follows PEP 8 guidelines.
- User Interaction: User menu is intuitive and allows testing of all functions.
  
🍀 Good luck, and happy coding! 🍀
