# 1) https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
def count(s):
    result = {}

    for char in s:
        found = False

        for key in result:
            if key == char:
                result[key] = result[key] + 1
                found = True

        if found == False:
            result[char] = 1

    return result

# 2) https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

result = ""
    
for letter in st:
        if letter == "a":
            result = result + "1"
        elif letter == "e":
            result = result + "2"
        elif letter == "i":
            result = result + "3"
        elif letter == "o":
            result = result + "4"
        elif letter == "u":
            result = result + "5"
        else:
            result = result + letter


    
def decode(st):
    result = ""
    
    for letter in st:
        if letter == "1":
            result = result + "a"
        elif letter == "2":
            result = result + "e"
        elif letter == "3":
            result = result + "i"
        elif letter == "4":
            result = result + "o"
        elif letter == "5":
            result = result + "u"
        else:
            result = result + letter

    return result

# 4) https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9/train/python
def sortme(words):
     return sorted(words, key=str.lower)