import re

numbers = input()
regex_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex_pattern, numbers)
print(', '.join(matches))