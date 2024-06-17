numbers_of_rooms = int(input())
free_chairs = 0
flag = False

for room_number in range(1, numbers_of_rooms + 1):
    chairs, number_of_visitors = input().split()

    diff = abs(len(chairs) - int(number_of_visitors))

    if len(chairs) < int(number_of_visitors):
        print(f'{diff} more chairs needed in room {room_number}')
        flag = True
    else:
        free_chairs += diff

if not flag:
    print(f'Game On, {free_chairs} free chairs left')