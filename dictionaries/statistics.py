stock = {}

while True:
    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(': ')
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

product_count = len(stock)
total_quantity = sum(stock.values())

print(f'Products in stock:')
for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_quantity}')

