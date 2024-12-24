# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
# Reversed Strings
def solution(string):
    return string[::-1]


# https://www.codewars.com/kata/544675c6f971f7399a000e79/train/python
# Convert a String to a Number!
def string_to_number(s):
    return int(s)


# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
# Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)


# https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/train/python
# MakeUpperCase
def make_upper_case(s):
    return s.upper()


# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"


# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
# Remove First and Last Character
def remove_char(s):
    return s[1:-1]