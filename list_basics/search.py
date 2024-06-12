n = int(input())
special_word = input()
strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)

filtered_strings = []

for string in strings:
    if special_word in string:
        filtered_strings.append(string)

print(strings)
print(filtered_strings)