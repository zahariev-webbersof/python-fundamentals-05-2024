class Party:
    def __init__(self):
        self.people = []

    def add_peron(self, name_):
        self.people.append(name_)

    def print_party_info(self):
        return f'Going: {", ".join(self.people)}\nTotal: {len(party_object.people)}'


party_object = Party()

while True:
    name = input()

    if name == 'End':
        break

    party_object.add_peron(name)

result = party_object.print_party_info()
print(result)
