# Test Judge System 📝🔰

The goal of this project is to build a system that automatically tests a user-provided solution against a predefined task and calculates the success rate of the tests. This project involves creating a testing framework using Python's unittest module, defining a task function, a user solution function, and a judge function to evaluate the solutions.

# ✅ Requirements

- Task Function (task_run):

  - This function should take input data as a string, process it, and return an output string.
  - Implement a sample task: Given a list of products and quantities, calculate the total quantity of each product and the total number of products.

- User Solution Function (user_solution_run):

  - This function should be similar to task_run but implemented by the user.
  - Ensure it processes the input data correctly and returns the expected output.
  - 
- Test Case Class (TestTask):

  - Define a class inheriting from unittest.TestCase.
  - Implement methods to test the task_run and user_solution_run functions.
  - Track the number of total tests and correct tests using class variables.

- Judge Function (judge):

  - Create a function to run all the test cases using unittest and calculate the success rate.
  - Print the total number of tests, the number of correct tests, and the success rate.

- Additional Features:

  - Implement a logging system to keep track of test results.
  - Add the ability to handle multiple test cases.
  - Create a user interface (CLI or web-based) for users to submit their solutions and view the results.
  - Use version control (Git) for collaborative development.

# ✅ Project Points

- Task Function Implementation (20 points)

  - Correctly processes the input data.
  - Generates the expected output format.
  - Handles edge cases (e.g., empty input, invalid data).

- User Solution Function (20 points)

  - Mimics the behavior of the task function.
  - Correctly processes the input data and generates the expected output.

- Test Case Class (30 points)

  - Implements unit tests for both task_run and user_solution_run.
  - Accurately tracks the number of tests and correct results.
  - Includes multiple test cases with varying input data.

- Judge Function (20 points)

  - Runs the test cases and calculates the success rate.
  - Outputs the results in a clear and concise manner.

- Additional Features (10 points)

  - Logging system for test results.
  - User interface for solution submission and result viewing.
  - Use of version control for collaborative development.


# ✅ Provided Skeleton Code
```python
import unittest
# 
# Define the task function (the problem statement)
def task_run(input_data):
    # Put the code from problem solution and return the result 

    # For example: 
    products = {}
    for line in input_data.split('\n'):
        if line == "statistics":
            break
        product, quantity = line.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    output = "Products in stock:\n"
    for product, quantity in products.items():
        output += f"- {product}: {quantity}\n"
    output += f"Total Products: {len(products)}\n"
    output += f"Total Quantity: {sum(products.values())}"
    return output

# User-provided solution (to be tested)
def user_solution_run(input_data):
    # Put the code from user solution and return the result

    # For example:
    products = {}
    for line in input_data.split('\n'):
        if line == "statistics":
            break
        product, quantity = line.split(': ')
        quantity = int(quantity)
        if product in products:
            products[product] += quantity
        else:
            products[product] = quantity

    output = "Products in stock:\n"
    for product, quantity in products.items():
        output += f"- {product}: {quantity}\n"
    output += f"Total Products: {len(products)}\n"
    output += f"Total Quantity: {sum(products.values())}"
    return output

# Define the test case for the task
class TestTask(unittest.TestCase):
    correct_tests = 0
    total_tests = 0

    # Put the test functions here
    # For Example:

    def run_test(self, func, input_data, expected_output):
            TestTask.total_tests += 1
            if func(input_data) == expected_output:
                TestTask.correct_tests += 1

    def test_task(self):
        input_data = "bread: 4\ncheese: 2\nham: 1\nbread: 1\nstatistics"
        expected_output = """Products in stock:
        - bread: 5
        - cheese: 2
        - ham: 1
        Total Products: 3
        Total Quantity: 8"""
    
    # Run the test for task_run function
        
    # Run the test for user_solution_run function

# Main judge function to run the tests
def judge():
    # Load the test cases from TestTask class
    
    # Run the test suite
    
    # Retrieve the correct and total tests count
    
    # Calculate and print the success rate

if __name__ == '__main__':
    judge()

```

# ✅ Additional options
If desired, functionality can be added to the project to test the user code through an API for the presence of code generated by artificial intelligence 

🍀 Good luck, and happy coding! 🍀
