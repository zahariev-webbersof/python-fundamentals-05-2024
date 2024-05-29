###### 1. Given the list my_list = ['a', 'b', 'a', 'c', 'a', 'b'], what will my_list.count('a') return?

- A: 1
- B: 2
- C: 3
- D: 4

<details><summary><b>Answer</b></summary> 
<p>

#### Correct Answer ->  C: 3

</p>
</details>

###### 2. What is the output of the following Python code?

```python
my_list = [1, 2, 3, 4, 5]
copied_list = my_list.copy()
copied_list.append(6)

```

- A: my_list is [1, 2, 3, 4, 5] and copied_list is [1, 2, 3, 4, 5, 6]
- B: my_list is [1, 2, 3, 4, 5, 6] and copied_list is [1, 2, 3, 4, 5, 6]
- C: my_list is [1, 2, 3, 4, 5] and copied_list is [6]
- D: my_list is [6] and copied_list is [1, 2, 3, 4, 5, 6]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: my_list is [1, 2, 3, 4, 5] and copied_list is [1, 2, 3, 4, 5, 6]

</p>
</details>

###### 3. Which method would you use to remove the first occurrence of a value in a list?

- A: remove()
- B: delete()
- C: pop()
- D: discard()

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: remove()

</p>
</details>

###### 4. Given the list my_list = [1, 2, 3, 4, 5], what will my_list.pop(1) return?

- A: 4
- B: 5
- C: 2
- D: 1

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: 2

</p>
</details>

###### 5. What is the result of the following code?

```python
my_list = [1, 2, 3, 4, 5]
my_list[1:4] = [10, 11, 12, 13]

```

- A: [1, 10, 11, 12, 13, 5]
- B: [1, 10, 11, 12, 5]
- C: [1, 2, 10, 11, 12, 13, 5]
- D: [1, 10, 11, 12, 13]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: [1, 10, 11, 12, 13, 5]

</p>
</details>

###### 6. Given the list my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], what does my_list.sort(reverse=True) do?

- A: Sorts the list in ascending order
- B: Sorts the list in descending order
- C: Reverses the list
- D: Raises a TypeError

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: Sorts the list in descending order

</p>
</details>

###### 7. Which of the following methods would you use to concatenate two lists?

- A: list1.append(list2)
- B: list1 + list2
- C: list1.extend(list2)
- D: Both b and c

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> D: Both b and c

</p>
</details>

###### 8. Given the list my_list = ['a', 'b', 'c', 'd', 'e'], what will my_list.index('c', 2) return?

- A: 2
- B: 3
- C: -1
- D: Raises a ValueError

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer ->  D: Raises a ValueError

</p>
</details>

###### 9. Given the list my_list = [1, 2, [3, 4], [5, [6, 7]]], what does my_list[3][1][0] return?

- A: 5
- B: 6
- C: 7
- D: [6, 7]


<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 6

</p>
</details>

###### 10. What is the output of the following code?

```python
my_list = [1, 2, 3]
copied_list = my_list[:]
copied_list.append(4)
my_list.append(5)

```

- A: my_list is [1, 2, 3, 4] and copied_list is [1, 2, 3, 4]
- B: my_list is [1, 2, 3, 5] and copied_list is [1, 2, 3, 4]
- C: my_list is [1, 2, 3, 4, 5] and copied_list is [1, 2, 3, 4]
- D: my_list is [1, 2, 3, 5] and copied_list is [1, 2, 3, 5]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: my_list is [1, 2, 3, 5] and copied_list is [1, 2, 3, 4]
</p>
</details>


###### 11. BONUS QUESTION -> What will be the output of the code snippet?

```python
a = [1, 2, 3]
b = a[:]
a[1] = 4
c = a + b
c[3] = 5
print(c)

```

- A: [1, 2, 3, 1, 2, 3]
- B: [1, 4, 3, 1, 2, 3]
- C: [1, 4, 3, 5, 2, 3]
- D: [1, 4, 3, 5, 4, 3]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 
</p>
</details>


###### 12. BONUS QUESTION -> What is the output of the following Python code?

```python
a = [1, 2, 3]
b = [a, a]
a[0] = 42
b[0][1] = 99
print(b)

```

- A: [[42, 99, 3], [1, 2, 3]]
- B: [[1, 99, 3], [1, 2, 3]]
- C: [[42, 99, 3], [42, 99, 3]]
- D: [[42, 2, 3], [42, 2, 3]]

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> You tell me :)) 

</p>
</details>
