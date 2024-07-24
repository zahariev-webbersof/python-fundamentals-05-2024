import re

data = input()

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

matches = re.finditer(pattern, data)

calories_counter = 0
food_items = []

for match in matches:
    item = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))

    calories_counter += calories
    food_items.append([item, expiration_date, calories])


days = calories_counter // 2000

print(f"You have food to last you for: {days} days!")

for item, expiration_date, calories in food_items:
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")

