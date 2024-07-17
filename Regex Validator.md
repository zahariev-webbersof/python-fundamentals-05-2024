# String Validation using Regular Expressions in Python 📝🔰

#### ✅ Objective:
The goal of this project is to create a Python script that validates different types of strings using regular expressions (regex). Improve your specifically focus on validating email addresses, phone numbers, and postal codes.

#### ✅ Project Requirements:
1. **Email Validation:**
   - An email address should follow the format `username@domain.extension`.
   - The `username` can contain letters, numbers, dots, hyphens, and underscores.
   - The `domain` can contain letters and numbers.
   - The `extension` should be 2-6 characters long and only contain letters.

2. **Phone Number Validation:**
   - A phone number should follow the format `XXX-XXX-XXXX` where `X` is a digit.

3. **Postal Code Validation:**
   - A postal code should be in the format `XXXXX` or `XXXXX-XXXX` where `X` is a digit.

#### ✅ Instructions:
1. **Regex Patterns:**
   - Students need to create regex patterns to match the required formats for email addresses, phone numbers, and postal codes.

2. **Function Definitions:**
   - Define separate functions for validating email, phone number, and postal code.
   - Each function should take a string as input and return `True` if the string matches the pattern, otherwise return `False`.

3. **User Input:**
   - Create a simple interface to accept user input for email, phone number, and postal code.
   - Validate the input using the defined functions and print appropriate messages.

#### ✅ Code Skeleton:
```python
import re

# Function to validate email addresses
def validate_email(email):
    """
    Validate the email address using regex.
    :param email: str - Email address to validate
    :return: bool - True if valid, False otherwise
    """
    # Define the regex pattern for a valid email address
   
    # Use re.match to check if the email matches the pattern
    return 

# Function to validate phone numbers
def validate_phone(phone):
    """
    Validate the phone number using regex.
    :param phone: str - Phone number to validate
    :return: bool - True if valid, False otherwise
    """
    # Define the regex pattern for a valid phone number
    
    # Use re.match to check if the phone matches the pattern
    return 

# Function to validate postal codes
def validate_postal_code(postal_code):
    """
    Validate the postal code using regex.
    :param postal_code: str - Postal code to validate
    :return: bool - True if valid, False otherwise
    """
    # Define the regex pattern for a valid postal code
    
    # Use re.match to check if the postal code matches the pattern
    return 

def main():
    """
    Main function to get user input and validate using the defined functions.
    """
    # Get email input from the user
    email = input("Enter your email address: ")
    # Validate the email and print the result
    if validate_email(email):
        print("The email address is valid.")
    else:
        print("The email address is invalid.")

    # Get phone number input from the user
    phone = input("Enter your phone number (XXX-XXX-XXXX): ")
    # Validate the phone number and print the result
    if validate_phone(phone):
        print("The phone number is valid.")
    else:
        print("The phone number is invalid.")

    # Get postal code input from the user
    postal_code = input("Enter your postal code (XXXXX or XXXXX-XXXX): ")
    # Validate the postal code and print the result
    if validate_postal_code(postal_code):
        print("The postal code is valid.")
    else:
        print("The postal code is invalid.")

# Call the main function
if __name__ == "__main__":
    main()
```

### ✅ Additional Information:
- **Regex Resources:**
  - Students can refer to [Regex101](https://regex101.com/) to test and understand regex patterns.
  - The [Python `re` module documentation](https://docs.python.org/3/library/re.html) provides detailed information on regex operations.

---
🍀 Good luck, and happy coding! 🍀
