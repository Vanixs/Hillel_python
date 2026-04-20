import string
import keyword

user_input = input()


def check_variable(name):
    if name in keyword.kwlist:
        return False
    if any(char.isupper() for char in name):
        return False
    if name[0].isdigit():
        return False
    if "__" in name:
        return False

    forbidden = string.punctuation.replace("_", "") + " "
    if any(char in forbidden for char in name):
        return False

    return True


print(check_variable(user_input))