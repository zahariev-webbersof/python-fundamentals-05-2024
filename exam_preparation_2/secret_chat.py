def insert_space(message, index):
    return message[:index] + ' ' + message[index:]


def reverse_substring(message, substring):
    if substring in message:
        message = message.replace(substring, '', 1)
        reversed_substring = substring[::-1]
        return message + reversed_substring
    else:
        return 'error'


def change_all(message, substring, replacement):
    return message.replace(substring, replacement)


def process_commands(message, commands):
    for command in commands:
        parts = command.split(':|:')
        action = parts[0]

        if action == 'InsertSpace':
            index = int(parts[1])
            message = insert_space(message, index)

        elif action == 'Reverse':
            substring = parts[1]
            result = reverse_substring(message, substring)
            if result == 'error':
                print('error')
                continue
            else:
                message = result
        elif action == 'ChangeAll':
            substring = parts[1]
            replacement = parts[2]
            message = change_all(message, substring, replacement)

        print(message)

    return message


secret_message = input()
all_commands = []

while True:
    command = input()
    if command == 'Reveal':
        break
    all_commands.append(command)

decrypt_message = process_commands(secret_message, all_commands)
print(f'You have a new text message: {decrypt_message}')
