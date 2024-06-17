def merge(data, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(len(data) - 1, end_index)

    if start_index < end_index:
        merged = ''.join(data[start_index:end_index + 1])
        data[start_index:end_index + 1] = [merged]


def divide(data, index, partitions):
    element = data[index]
    part_length = len(element) // partitions

    divided_parts = []
    start = 0

    for i in range(partitions):
        if i == partitions - 1:
            divided_parts.append(element[start:])
        else:
            divided_parts.append(element[start:start + part_length])
            start += part_length

    data[index:index + 1] = divided_parts



def process_commands(data, commands):
    for command in commands:
        parts = command.split()

        if parts[0] == 'merge':
            start_index = int(parts[1])
            end_index = int(parts[2])
            merge(data, start_index, end_index)

        elif parts[0] == 'divide':
            index = int(parts[1])
            partitions = int(parts[2])
            divide(data, index, partitions)

    return data


data = input().split()
commands = []

while True:
    command = input()

    if command == '3:1':
        break

    commands.append(command)

result = process_commands(data, commands)
print(' '.join(result))