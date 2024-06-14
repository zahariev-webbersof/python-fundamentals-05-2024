def check_employee_happiness(happiness_list, happiness_factor):
    improved_happiness = [happiness_factor * current_value for current_value in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(num >= average_happiness for num in improved_happiness)
    total_count = len(improved_happiness)

    message = 'happy' if happy_count >= total_count / 2 else 'not happy'

    return f'Score: {happy_count}/{total_count}. Employees are {message}!'


happiness_lst = list(map(int, input().split()))
num_factor = int(input())
result = check_employee_happiness(happiness_lst, num_factor)
print(result)