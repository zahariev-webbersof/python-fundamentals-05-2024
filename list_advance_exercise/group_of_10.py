def group_numbers(numbers):
    group_boundary = 10
    result = []

    while numbers:
        group = [num for num in numbers if num <= group_boundary]

        numbers = [num for num in numbers if num > group_boundary]

        result.append(f"Group of {group_boundary}'s: {group}")

        group_boundary += 10

    for group in result:
        print(group)


input_strings = list(map(int, input().split(', ')))
group_numbers(input_strings)