data = input().split()

stock = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i + 1])
    stock[food] = quantity

print(stock)