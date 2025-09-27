# I) Easy Codewars 8 kuy:
# https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python
def is_uppercase(inp):
    if inp == inp.upper():
        return True
    else:
        return False

# https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python
def move(position, roll):
    return position + roll * 2

# II) Easy Codewars 7 kyu:
# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    
    result = ""
    
    for i in string_:
        if i not in vowels:
            result += i
    return result

# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    s = s.lower()
    x = 0
    o = 0
    
    for i in s:
        if i == "x":
            x += 1
        elif i == "o":
            o += 1
    return x == o

# III) Hard Codewars 8 kuy:
# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

# IV) Hard Codewars 7 kuy:
# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    s = str(n)
    digits = []
    
    for i in s:
        digits.append(int(i))
        
    digits.reverse()
    
    return digits

# V) Boss Level:
# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/train/python
def max_diff(lst):
    if len(lst) == 0:
        return 0
    return max(lst) - min(lst)