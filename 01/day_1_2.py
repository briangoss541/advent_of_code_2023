with open('input.txt') as in_file:
    input_strings = in_file.readlines()

# input_strings = [
# 'two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen'
# ]

values_list = list()

spelled_letters = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

for input_string in input_strings:

    string_list = list(input_string)

    start_value = None
    end_value = None

    for string_index, x in enumerate(string_list):
        if x.isdigit():
            start_value = x
        for spelled_letter in spelled_letters:
            if spelled_letter in ''.join(string_list[:string_index]):
                start_value = spelled_letters[spelled_letter]
                break
        if start_value is not None:
            break

    for string_index in range(len(string_list) - 1, -1, -1):
        y = string_list[string_index]
        if y.isdigit():
            end_value = y
        for spelled_letter in spelled_letters:
            if spelled_letter in ''.join(string_list[string_index:]):
                end_value = spelled_letters[spelled_letter]
                break
        if end_value is not None:
            break

    values_list.append(int(str(start_value) + str(end_value)))

print(values_list)
print(sum(values_list))
