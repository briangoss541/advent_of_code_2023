with open('input.txt') as in_file:
    input_list = in_file.readlines()

# input_list = [
# 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
# ]

games_list = list()

for input_row in input_list:

    game_text, set_text = input_row.split(': ')
    game_num = int(game_text.split(' ')[1])

    row_dict = {
        'game_num': game_num,
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for round_text in set_text.split(';'):

        for sub_set_text in round_text.split(', '):

            pull_num, pull_color = sub_set_text.strip().split(' ')

            pull_num = int(pull_num)

            if row_dict[pull_color] < pull_num:
                row_dict[pull_color] = pull_num

    games_list.append(row_dict)

print(games_list)

target_ceiling = {
    'red': 12,
    'green': 13,
    'blue': 14
}

passing_games = list()
for game_data in games_list:

    game_flag = True

    for target_color in target_ceiling:
        if game_data[target_color] > target_ceiling[target_color]:
            game_flag = False

    if game_flag:
        passing_games.append(game_data['game_num'])

print(sum(passing_games))
