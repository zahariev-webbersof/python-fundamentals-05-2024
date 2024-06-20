class BattleGame:
    def __init__(self, initial_energy):
        self.energy = initial_energy
        self.won_battles = 0

    def play(self):
        while True:
            command = input()

            if command == 'End of battle':
                return f'Won battles: {self.won_battles}. Energy left: {self.energy}'

            distance = int(command)

            if self.energy >= distance:
                self.won_battles += 1
                self.energy -= distance

                if self.won_battles % 3 == 0:
                    self.energy += self.won_battles

            else:
                return f'Not enough energy! Game ends with {self.won_battles} won battles and {self.energy} energy'


def main():
    enegry = int(input())
    game = BattleGame(enegry)
    result = game.play()
    print(result)


if __name__ == '__main__':
    main()