def add_lesson(schedule, lesson_title):
    if lesson_title not in schedule:
        schedule.append(lesson_title)


def insert_lesson(schedule, lesson_title, index):
    if lesson_title not in schedule:
        schedule.insert(index, lesson_title)


def remove_lesson(schedule, lesson_title):
    if lesson_title in schedule:
        schedule.remove(lesson_title)
        exercise_title = lesson_title + '-Exercise'
        if exercise_title in schedule:
            schedule.remove(exercise_title)


def swap_lesson(schedule, lesson1, lesson2):
    if lesson1 in schedule and lesson2 in schedule:
        idx1, idx2 = schedule.index(lesson1), schedule.index(lesson2)

        schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]

        exercise1, exercise2 = lesson1 + '-Exercise', lesson2 + '-Exercise'

        if exercise1 in schedule:
            schedule.remove(exercise1)
            schedule.insert(schedule.index(lesson1) + 1, exercise1)

        if exercise2 in schedule:
            schedule.remove(exercise2)
            schedule.insert(schedule.index(lesson2) + 1, exercise2)


def add_exercise(schedule, lesson_title):
    exercise_title = lesson_title + '-Exercise'
    if lesson_title in schedule:
        lesson_index = schedule.index(lesson_title)
        if exercise_title not in schedule:
            schedule.insert(lesson_index + 1, exercise_title)
    else:
        schedule.append(lesson_title)
        schedule.append(exercise_title)


def process_commands(schedule, commands):
    for command in commands:
        parts = command.split(':')
        action = parts[0]

        if action == 'Add':
            lesson_title = parts[1]
            add_lesson(schedule, lesson_title)

        elif action == 'Insert':
            lesson_title = parts[1]
            index = int(parts[2])
            insert_lesson(schedule, lesson_title, index)

        elif action == 'Remove':
            lesson_title = parts[1]
            remove_lesson(schedule, lesson_title)

        elif action == 'Swap':
            lesson1 = parts[1]
            lesson2 = parts[2]
            swap_lesson(schedule, lesson1, lesson2)

        elif action == 'Exercise':
            lesson_title = parts[1]
            add_exercise(schedule, lesson_title)

    return schedule


initial_schedule = input().split(', ')
commands = []

while True:
    command = input()
    if command == 'course start':
        break

    commands.append(command)


final_schedule = process_commands(initial_schedule, commands)
for index, lesson in enumerate(final_schedule, 1):
    print(f'{index}.{lesson}')