message = input()

while True:
    command = input()
    if command == 'Reveal':
        break

    parts = command.split(':|:')
    action = parts[0]

    if action == 'InsertSpace':
        index = int(parts[1])
        message = message[:index] + ' ' + message[index:]

    elif action == 'Reverse':
        substring = parts[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            reversed_substring = substring[::-1]
            message = message + reversed_substring
        else:
            print('error')

    elif action == 'ChangeAll':
        substring = parts[1]
        replacement = parts[2]
        message = message.replace(substring, replacement)

    print(message)

print(f'You have a new text message: {message}')