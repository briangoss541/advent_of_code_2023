from functools import reduce

with open('input.txt') as in_file:
    input_text = [x.strip() for x in in_file.readlines()]

# input_text = [
#     'Time:      7  15   30',
#     'Distance:  9  40  200'
# ]

times = [int(x) for x in input_text[0].split(':')[1].split(' ') if x.isdigit()]
distances = [int(x) for x in input_text[1].split(':')[1].split(' ') if x.isdigit()]

print(times)
print(distances)

race_list = list()
for idx in range(len(times)):

    current_record = distances[idx]
    viable_presses = 0
    for press in range(1, times[idx]):
        distance = press * (times[idx] - press)

        if distance > current_record:
            viable_presses += 1

    race_list.append(viable_presses)

print(reduce(lambda x, y: x * y, race_list))
