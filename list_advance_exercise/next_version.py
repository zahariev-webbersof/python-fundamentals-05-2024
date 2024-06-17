data = input().split('.')  # ['1', '9', '9'] - > 199 + 1 = 200
next_version = int(''.join(data)) + 1  # 200 -> ['2', '0', '0'] -> join('.')
print('.'.join(str(next_version)))