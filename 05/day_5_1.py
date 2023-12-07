with open('input.txt') as in_file:
    input_text = [x.strip() for x in in_file.readlines()]

# input_text = [
#     'seeds: 79 14 55 13',
#     '',
#     'seed-to-soil map:',
#     '50 98 2',
#     '52 50 48',
#     '',
#     'soil-to-fertilizer map:',
#     '0 15 37',
#     '37 52 2',
#     '39 0 15',
#     '',
#     'fertilizer-to-water map:',
#     '49 53 8',
#     '0 11 42',
#     '42 0 7',
#     '57 7 4',
#     '',
#     'water-to-light map:',
#     '88 18 7',
#     '18 25 70',
#     '',
#     'light-to-temperature map:',
#     '45 77 23',
#     '81 45 19',
#     '68 64 13',
#     '',
#     'temperature-to-humidity map:',
#     '0 69 1',
#     '1 0 69',
#     '',
#     'humidity-to-location map:',
#     '60 56 37',
#     '56 93 4',
# ]

seeds_text = input_text[0].replace('seeds: ', '')
seeds = [int(x) for x in seeds_text.split(' ')]

planting_data = {x: {0: x} for x in seeds}

# print(seeds)
# print(planting_data)

round_num = 0
changed_in_round = set()
for row in input_text:

    if 'map' in row:

        for record_id in planting_data.keys():
            planting_data[record_id][round_num + 1] = planting_data[record_id][round_num]

        round_num += 1
        changed_in_round = set()
        continue
    elif bool(row) is False or 'seeds' in row:
        continue

    dest_start, source_start, range_len = (int(x) for x in row.split(' '))

    for record_id, planting_record in planting_data.items():

        if record_id == 14 and round_num == 3:
            hello = 'hello'

        if (source_start <= planting_record[round_num] <= source_start + range_len - 1
                and record_id not in changed_in_round):
            planting_record[round_num] = dest_start + (planting_record[round_num] - source_start)
            changed_in_round.add(record_id)

# for thing in planting_data:
#     print(thing, planting_data[thing])

all_locations = [x[round_num] for x in planting_data.values()]

print(min(all_locations))
