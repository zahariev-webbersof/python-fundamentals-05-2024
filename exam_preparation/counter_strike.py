def battle_game(energy):
    won_battles = 0

    while True:
        command = input()

        if command == 'End of battle':
            return f'Won battles: {won_battles}. Energy left: {energy}'

        distance = int(command)

        if energy >= distance:
            won_battles += 1
            energy -= distance

            if won_battles % 3 == 0:
                energy += won_battles

        else:
            return f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy'


initial_energy = int(input())
result = battle_game(initial_energy)
print(result)