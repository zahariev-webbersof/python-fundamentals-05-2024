# "multiply", "divide", "add", and "subtract".

def calculate_result(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'add': num1 + num2,
        'subtract': num1 - num2,
    }.get(operator, 'Invalid operator!')


operator = input('Enter the operator (multiply, divide, add, subtract): ')
first_number = int(input('Enter the first value: '))
second_number = int(input('Enter the second value: '))
result = calculate_result(operator, first_number, second_number)
print(result)
