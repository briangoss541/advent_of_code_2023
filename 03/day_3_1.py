from itertools import product

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

x_max = len(input_text)
y_max = len(input_text[0])

adjacent_set = set()
for x_coord in range(len(input_text)):

    for y_coord in range(len(input_text[0])):

        for x_move, y_move in move_set:

            new_x = x_coord + x_move
            new_y = y_coord + y_move

            if new_x in range(0, x_max) and new_y in range(0, y_max):

                if not input_text[new_x][new_y].isdigit() and input_text[new_x][new_y] != '.':
                # if input_text[new_x][new_y] != '.':
                    adjacent_set.add(
                        (x_coord, y_coord)
                    )

parts_list = list()
for row_x, row in enumerate(input_text):

    current_number = list()
    number_coords = set()

    for row_y, target_char in enumerate(row):

        if not target_char.isdigit() or row_y == y_max - 1:

            if row_y == y_max - 1 and target_char.isdigit():
                current_number.append(target_char)
                number_coords.add((row_x, row_y))

            if len(current_number) > 0:
                if len(number_coords & adjacent_set) > 0:
                    parts_list.append(int(''.join(current_number)))
                    print('***' + ''.join(current_number))
                else:
                    print(int(''.join(current_number)))

            current_number = list()
            number_coords = set()
        else:
            current_number.append(target_char)
            number_coords.add((row_x, row_y))

print(parts_list)
print(sum(parts_list))
