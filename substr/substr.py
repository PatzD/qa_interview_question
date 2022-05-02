def check_repeat(original_string):

    string = original_string.lower()
    curr_len = 0
    curr_str = ''
    max_len = 0
    longest_str = ''


    for letter in string:
        if letter not in curr_str:
            curr_str += letter
            curr_len += 1

        elif letter in curr_str:
            if curr_len > max_len:
                longest_str = curr_str
                max_len = curr_len
                curr_str = ''
                curr_len = 0

    return [longest_str, max_len]


string_to_check = ''
a, b = check_repeat(string_to_check)
print(f'The answer is {a}, with a length of {b}')

