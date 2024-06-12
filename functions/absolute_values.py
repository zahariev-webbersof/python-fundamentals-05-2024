numbers = input().split()

absolute_values = []

for num in numbers:
    absolute_values.append(abs(float(num)))

print(absolute_values)