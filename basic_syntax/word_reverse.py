word = input()

for i in range(len(word) -1, -1, -1):
    print(word[i], end='')




#  Python Slice Notation
#  https://sentry.io/answers/python-slice-notation/
word = input()
print(word[::-1])
