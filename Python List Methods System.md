# Implementing Python List Methods 📝

Develop a console-based application that allows users to perform various operations on a list. The application will present a menu of options, each corresponding to a different list method. 
Users can choose an option by entering a number, and the application will execute the corresponding list method.


## ✅ Requirements:
1. Initial List Input:

- Prompt the user to input initial values for the list. These values should be comma-separated.

2. Menu Display:

- Display a list of options for the user, each corresponding to a list method.
Allow the user to select an option by entering the associated number.

3. List Methods to Implement:

- append()
- extend()
- insert()
- remove()
- pop()
- clear()
- index()
- count()
- sort()
- reverse()
- copy()

4. User Interaction:

- Prompt the user for necessary inputs based on the selected list method.
- Display the updated list after each operation.
- Include an option to exit the application.

5. Error Handling:

- Handle invalid inputs gracefully (e.g., non-integer menu choices, out-of-range indices).
- Provide meaningful error messages and prompt the user to try again.

6. Code Structure:

- Use functions to organize the code (e.g., separate functions for displaying the menu, handling each list method, etc.).
- Ensure the code is modular, readable, and well-documented.

## ✅ Additional Information:

- User Guidance: Provide clear instructions to the user on how to interact with the application (e.g., input formats, expected actions).

## Task Skeleton:
```python

def display_menu():
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")

def handle_append(lst):
    # TODO: Prompt the user for a value to append to the list
    # Use the append() method to add the value to the list
    # Print the updated list
    pass

def handle_extend(lst):
    # TODO: Prompt the user for values to extend the list (comma-separated)
    # Use the extend() method to add these values to the list
    # Print the updated list
    pass

def handle_insert(lst):
    # TODO: Prompt the user for an index and a value to insert at that index
    # Use the insert() method to add the value at the specified index
    # Print the updated list
    pass

def handle_remove(lst):
    # TODO: Prompt the user for a value to remove from the list
    # Use the remove() method to delete the first occurrence of the value
    # Handle the case where the value is not found in the list
    # Print the updated list
    pass

def handle_pop(lst):
    # TODO: Prompt the user for an index to pop (optional, leave empty to pop last item)
    # Use the pop() method to remove the item at the specified index or the last item if no index is provided
    # Handle the case where the index is out of range
    # Print the updated list
    pass

def handle_clear(lst):
    # TODO: Use the clear() method to remove all items from the list
    # Print the updated list
    pass

def handle_index(lst):
    # TODO: Prompt the user for a value to find its index
    # Use the index() method to find the index of the value
    # Handle the case where the value is not found in the list
    # Print the index of the value
    pass

def handle_count(lst):
    # TODO: Prompt the user for a value to count its occurrences in the list
    # Use the count() method to count how many times the value appears in the list
    # Print the count of the value
    pass

def handle_sort(lst):
    # TODO: Use the sort() method to sort the list in ascending order
    # Print the updated list
    pass

def handle_reverse(lst):
    # TODO: Use the reverse() method to reverse the order of the list
    # Print the updated list
    pass

def handle_copy(lst):
    # TODO: Use the copy() method to create a shallow copy of the list
    # Print the copied list
    pass

def main():
    initial_values = input("Enter initial list values (comma-separated): ")
    lst = initial_values.split(',')
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        if choice == '1':
            handle_append(lst)
        elif choice == '2':
            handle_extend(lst)
        elif choice == '3':
            handle_insert(lst)
        elif choice == '4':
            handle_remove(lst)
        elif choice == '5':
            handle_pop(lst)
        elif choice == '6':
            handle_clear(lst)
        elif choice == '7':
            handle_index(lst)
        elif choice == '8':
            handle_count(lst)
        elif choice == '9':
            handle_sort(lst)
        elif choice == '10':
            handle_reverse(lst)
        elif choice == '11':
            handle_copy(lst)
        elif choice == '12':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## Instructions for Students:

- Understand the Task: Read through the task description and requirements carefully.
- Implement the Functions: Write code for each list method as indicated by the TODO comments. Modify the skeleton to include user prompts and handle inputs appropriately.
- Test Your Code: Run the application and test each list method by selecting different options from the menu.
- Error Handling: Ensure your code handles invalid inputs gracefully and provides clear error messages.
- Submit Your Work: Submit your final code along with a brief documentation of how your application works and any challenges you faced.
