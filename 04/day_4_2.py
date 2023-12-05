# with open('input.txt') as in_file:
#     input_text = [x.strip() for x in in_file.readlines()]

input_text = [
'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]

card_tracker = dict()
for input_card in input_text:

    card_text, number_text = input_card.split(': ')
    card_num = int(card_text.split(' ')[-1])

    winning_text, have_text = number_text.split(' | ')
    winning_numbers = [int(x) for x in winning_text.split(' ') if x.isdigit()]
    have_numbers = [int(x) for x in have_text.split(' ') if x.isdigit()]

    card_tracker[card_num] = len(set(winning_numbers) & set(have_numbers))

card_counter = {k: 1 for k in card_tracker}

for focus_card, match_count in card_tracker.items():

    for _ in range(card_counter[focus_card]):
        for card_offset in range(1, match_count + 1):
            card_counter[focus_card + card_offset] += 1

print(sum(card_counter.values()))
