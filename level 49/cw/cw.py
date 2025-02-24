# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python
def replace_exclamation(st):
    result = ""
    for i in st:
        if i in "aeiouAEIOU":
            result += "!"
        else:
            result += i
    return result