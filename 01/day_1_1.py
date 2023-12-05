with open('input.txt') as in_file:
    input_strings = in_file.readlines()

# test_string = 'pqr3stu8vwx'

# string_list = list(test_string)

values_list = list()

for input_string in input_strings:

    string_list = list(input_string)

    start_value = None
    end_value = None
    for x in string_list:
        if x.isdigit():
            start_value = x
            break

    for y in reversed(string_list):
        if y.isdigit():
            end_value = y
            break

    values_list.append(int(str(start_value) + str(end_value)))

print(sum(values_list))
