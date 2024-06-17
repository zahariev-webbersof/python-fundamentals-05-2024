data = input().split()
result = [word for word in data if len(word) % 2 == 0]
print('\n'.join(result))