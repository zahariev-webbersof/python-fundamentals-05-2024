waiting_people = int(input())
current_state_of_the_lift = list(map(int, input().split()))

for i in range(len(current_state_of_the_lift)):
    if waiting_people > 3:
        current_number_of_people = abs(4 - int(current_state_of_the_lift[i]))
        waiting_people -= current_number_of_people
        current_state_of_the_lift[i] += current_number_of_people
    else:
        current_state_of_the_lift[i] += waiting_people


if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
    print(f'The lift has empty spots!')

print(' '.join(str(num) for num in current_state_of_the_lift))


