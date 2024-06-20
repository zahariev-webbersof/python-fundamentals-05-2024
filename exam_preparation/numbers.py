numbers = list(map(int, input().split()))
average_sum = sum(numbers) / len(numbers) if numbers else 0
greater_numbers_than_average_sum = [num for num in numbers if num > average_sum]

if greater_numbers_than_average_sum:
    top_numbers = sorted(greater_numbers_than_average_sum, reverse=True)[:5]
    print(' '.join(map(str, top_numbers)))
else:
    print('No')