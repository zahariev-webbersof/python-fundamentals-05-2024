###### 1. How do you declare a string variable in Python?

- A: By assigning a number directly to the variable.
- B: By enclosing the text in single or double quotes (e.g., name = "Alice").
- C: Using a dedicated string data type declaration.
- D: Using a container to store string data in your program

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer ->  B: By enclosing the text in single or double quotes (e.g., name = "Alice").

</p>
</details>

###### 2. What is the output of the following code?

```python
my_dict = {"fruit": "apple"}
my_dict["fruit"] = "banana"
print(my_dict["fruit"])

```

- A: An error, you cannot modify dictionaries.
- B: "apple" (original value)
- C: "banana" (modified value)
- D: It will print the entire dictionary.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: "banana" (modified value)

</p>
</details>

###### 3. How can you check the data type of a variable in Python?

- A: By using a specific function to define the data type.
- B: There's no way to check the data type in Python.
- C: The data type is automatically determined at runtime.
- D: By using the type() function (e.g., print(type(variable_name))).

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: By using the type() function (e.g., print(type(variable_name))).

</p>
</details>

###### 4. What is the difference between mutable and immutable data types in Python?

- A: There's no such distinction in Python.
- B: Mutable data types can be changed after creation, while immutable ones cannot.
- C: Mutable data types are faster for performance reasons.
- D: Immutable data types are used for storing user input.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> Mutable data types (like lists, dictionaries) can be modified after creation, while immutable ones (like strings, numbers, tuples) cannot have their elements changed.

</p>
</details>

###### 5. How can you convert a string containing comma-separated numbers into a list of integers?

- A: There's no built-in way to do this directly.
- B: Use a loop to split the string and convert each element to an integer.
- C: Use the split() method on the string and then int() on each element to create a list of integers.
- D: None of this

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Use the split() method on the string and then int() on each element to create a list of integers.

</p>
</details>

###### 6. How can you iterate over elements in a list while modifying them simultaneously?

- A: You cannot modify elements while iterating in Python.
- B: You need to create a separate loop for modification.
- C: Use a for i in range(len(list)) loop to access indices and modify elements.
- D: Use a for element in list loop. This iterates directly over the elements, allowing in-place modification.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: Use a for element in list loop. This iterates directly over the elements, allowing in-place modification.

</p>
</details>

###### 7. What happens when you try to access an element outside the list's index range?

- A: The element is automatically created at that index.
- B: The code silently ignores the out-of-range access.
- C: You will get an IndexError exception.
- D: The program crashes.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: You will get an IndexError exception.

</p>
</details>

###### 8. What is the concept of type hinting in Python, and how is it beneficial?

- A: Type hinting is a way to force specific data types during variable declaration (not enforced).
- B: Type hinting is a way to provide optional type annotations for variables and function arguments, improving code readability and potential static type checking with external tools.
- C: It's a mandatory requirement for Python programs.
- D: It allows for faster code execution.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Type hinting is a way to provide optional type annotations for variables and function arguments, improving code readability and potential static type checking with external tools.

</p>
</details>

###### 9. How can you deep copy a nested data structure (list of dictionaries) in Python to avoid unintended modifications?

- A: Copying the reference is sufficient, as changes won't affect the original.
- B: Use a loop to manually copy each element and create a new structure.
- C: There's no built-in way to achieve a deep copy.
- D: Use the copy module's deepcopy() function to create a new, independent copy of the entire nested structure.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: Use the copy module's deepcopy() function to create a new, independent copy of the entire nested structure.

</p>
</details>

###### 10. How can you convert a string representation of a number (e.g., "123") to an actual integer in Python?

- A: number = "123"
- B: number = int("123")
- C: number = number + 0
- D: number = number('123')

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> number = int("123")
</p>
</details>
