import pandas as pd

with open('input.txt') as in_file:
    input_text = [x.strip() for x in in_file.readlines()]

# input_text = [
# '32T3K 765',
# 'T55J5 684',
# 'KK677 28',
# 'KTJJT 220',
# 'QQQJA 483',
# ]


def score_hand(input_series):

    value_dict = {
        'A': 13,
        'K': 12,
        'Q': 11,
        'J': 1,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    top_score = 0
    if 'J' in input_series.values:

        for joker in value_dict.keys():

            test_series = input_series.replace('J', joker)

            hand_count = test_series.value_counts()
            hand_score = 0

            if hand_count.iloc[0] == 5:
                hand_score += 7 * 10**10
            elif hand_count.iloc[0] == 4:
                hand_score += 6 * 10**10
            elif hand_count.iloc[0] == 3 and hand_count.iloc[1] == 2:
                hand_score += 5 * 10**10
            elif hand_count.iloc[0] == 3:
                hand_score += 4 * 10**10
            elif hand_count.iloc[0] == 2 and hand_count.iloc[1] == 2:
                hand_score += 3 * 10**10
            elif hand_count.iloc[0] == 2:
                hand_score += 2 * 10**10

            if hand_score > top_score:
                top_score = hand_score

    else:
        hand_count = input_series.value_counts()
        hand_score = 0

        if hand_count.iloc[0] == 5:
            hand_score += 7 * 10 ** 10
        elif hand_count.iloc[0] == 4:
            hand_score += 6 * 10 ** 10
        elif hand_count.iloc[0] == 3 and hand_count.iloc[1] == 2:
            hand_score += 5 * 10 ** 10
        elif hand_count.iloc[0] == 3:
            hand_score += 4 * 10 ** 10
        elif hand_count.iloc[0] == 2 and hand_count.iloc[1] == 2:
            hand_score += 3 * 10 ** 10
        elif hand_count.iloc[0] == 2:
            hand_score += 2 * 10 ** 10

        top_score = hand_score

    for i, places in enumerate([8, 6, 4, 2, 0]):
        top_score += value_dict.get(input_series.iloc[i]) * 10**places

    return top_score


hand_dict = dict()
bid_amount = list()
for i, row in enumerate(input_text):
    hand_chars = row.split(' ')[0]
    hand_dict[i] = list(hand_chars)
    bid_amount.append(int(row.split(' ')[1]))

scored_dict = dict()
for hand_id, hand_data in hand_dict.items():
    hand = pd.Series(hand_data)
    scored_hand = score_hand(hand)
    scored_dict[hand_id] = scored_hand

sorted_ids = [k for k, v in sorted(scored_dict.items(), key=lambda item: item[1])]

total_winnings = 0
for idx, hand_id in enumerate(sorted_ids):
    print(hand_dict[hand_id])
    total_winnings += bid_amount[hand_id] * (idx + 1)

print(total_winnings)
