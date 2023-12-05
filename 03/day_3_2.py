from itertools import product
from collections import defaultdict

with open('input.txt') as in_file:
    input_text = [x.strip() for x in in_file.readlines()]

# input_text = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..'
# ]

move_set = {(x, y) for x, y in product([-1, 0, 1], repeat=2)} - {(0, 0)}

# Resetting x and y!

x_max = len(input_text[0])
y_max = len(input_text)

adjacent_set = set()
gear_set = set()
gear_dict = defaultdict(set)
for y_coord in range(y_max):

    for x_coord in range(x_max):

        for x_move, y_move in move_set:

            new_x = x_coord + x_move
            new_y = y_coord + y_move

            if new_x in range(0, x_max) and new_y in range(0, y_max) and input_text[new_y][new_x] == '*':
                gear_dict[(new_x, new_y)].add((x_coord, y_coord))

print(gear_dict)

gear_part_dict = defaultdict(list)
for row_y, row in enumerate(input_text):

    current_number = list()
    number_coords = set()

    for row_x, target_char in enumerate(row):

        if not target_char.isdigit() or row_x == x_max - 1:

            if row_x == x_max - 1 and target_char.isdigit():
                current_number.append(target_char)
                number_coords.add((row_x, row_y))

            if len(current_number) > 0:

                for gear_coord, gear_adjacent in gear_dict.items():

                    if len(number_coords & gear_adjacent) > 0:
                        gear_part_dict[gear_coord].append(int(''.join(current_number)))

            current_number = list()
            number_coords = set()
        else:
            current_number.append(target_char)
            number_coords.add((row_x, row_y))

overall_power = 0
for gear_coord, part_list in gear_part_dict.items():
    if len(part_list) == 2:
        overall_power += (part_list[0] * part_list[1])

print(overall_power)
