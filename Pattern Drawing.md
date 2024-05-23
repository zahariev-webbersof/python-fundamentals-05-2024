# Task: Python Pattern Drawing

Create six different patterns using Python's printing capabilities.



### Pattern 1: Right-angled Triangle

Develop a Python script that generates a right-angled triangle pattern. The script should prompt the user to specify the number of rows. Here's a sample output for a user input of 5:

```
*
**
***
****
*****
```
### Solution
n = int(input())
for i in range(n + 1):
	print(i * '*')
 
### Pattern 2: Square with Hollow Center

Craft a Python program that produces a square pattern with a hollow center. The program should take the size of the square as input from the user. Here's an example output for a user input of 5:

```
*****
*   *
*   *
*   *
*****
```
### Solution
n = int(input())
for i in range(n - (n - 2) - 1):
	print(n * '*')
for j in range(n - 2):
	print('*' + (n - 2) * ' ' + '*')
print(n * '*')

### Pattern 3: Diamond

Write a Python script that displays a diamond pattern based on the number of rows (height) specified by the user. For instance, if the user enters 5, the output should resemble the following:

```
  *
 ***
*****
 ***
  *
```
### Hint
# 3, 2, 1, 0, 1, 2, 3  space
# 1, 3, 5, 7, 5, 3, 1  star

### Solution
n = int(input())
for i in range(n):
    print(' ' * (n - i),  '*' * (i * 2 + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i),  '*' * (i * 2 + 1))
    
### Pattern 4: Left-angled Triangle

Design a Python code snippet to print a left-angled triangle pattern. The user should provide the number of rows. For instance, if the user inputs 4, the output should be:

```
****
***
**
*
```
### Solution
n = int(input())
for i in range(n + 1):
	print((n - i) * '*')
 
### Pattern 5: Hollow Square

Implement a Python program that prints a square pattern with a hollow center, where the user specifies the size of the square. For example, if the user inputs 6, the output should be:

```
******
*    *
*    *
*    *
*    *
******
```
### Solution
n = int(input())
for i in range(n - (n - 2) - 1):
	print(n * '*')
for j in range(n - 2):
	print('*' + (n - 2) * ' ' + '*')
print(n * '*')

### Pattern 6: Pyramid

Create a Python script that prints a pyramid pattern based on the user-input number of rows. For example, if the user inputs 4, the output should be:

```
   *
  ***
 *****
*******
```
### Hint
# 3, 2, 1, 0  space
# 1, 3, 5, 7  star

### Solution
n = int(input())
for i in range(n):
    print(' ' * (n - i),  '*' * (i * 2 + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i),  '*' * (i * 2 + 1))
➡ Instructions:

1. Utilize nested loops to control the row and column structure of each pattern.
2. Use the print function to output patterns. For spacing, consider using either the space character (" ") or tabs ("\t").
3. Prompt the user to enter the necessary parameters for each pattern.
