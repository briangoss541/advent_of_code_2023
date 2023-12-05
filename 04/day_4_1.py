with open('input.txt') as in_file:
    input_text = [x.strip() for x in in_file.readlines()]

# input_text = [
# 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
# 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
# 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
# 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
# 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
# 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
# ]

card_tracker = dict()
for input_card in input_text:

    card_text, number_text = input_card.split(': ')
    card_num = int(card_text.split(' ')[-1])

    winning_text, have_text = number_text.split(' | ')
    winning_numbers = [int(x) for x in winning_text.split(' ') if len(x) > 0]
    have_numbers = [int(x) for x in have_text.split(' ') if len(x) > 0]

    overlapping_numbers = set()
    for overlap_num in set(winning_numbers) & set(have_numbers):
        overlapping_numbers.add(overlap_num)

    card_tracker[card_num] = overlapping_numbers

print(card_tracker)

scratch_total = 0
for matching_cards in card_tracker.values():
    if len(matching_cards) == 0:
        continue
    elif len(matching_cards) == 1:
        scratch_total += 1
    else:
        scratch_total += 2**(len(matching_cards) - 1)

print(scratch_total)
