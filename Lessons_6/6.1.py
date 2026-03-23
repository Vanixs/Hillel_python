import string

def get_char_range(range_str):
    start, end = range_str.split('-')
    all_letters = string.ascii_letters
    return all_letters[all_letters.index(start) : all_letters.index(end) + 1]

user_input = input()
print(get_char_range(user_input))