import re

text = 'Apple, apple and APPLE are the same fruit.'

pattern = r'apple'

match = re.findall(pattern, text, re.IGNORECASE)

print(match)