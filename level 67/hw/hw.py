# 1) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
     return ' '.join(word.capitalize() for word in string.split())

# 2) https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
def get_sum(a,b):
    if a > b:
        a, b = b, a 
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

# 3) https://www.codewars.com/kata/5663f5305102699bad000056/train/python
def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    max1 = 0
    min1 = len(a1[0])
    for word in a1:
        length = len(word)
        if length > max1:
            max1 = length
        if length < min1:
            min1 = length

    max2 = 0
    min2 = len(a2[0])
    for word in a2:
        length = len(word)
        if length > max2:
            max2 = length
        if length < min2:
            min2 = length

    diff1 = max1 - min2
    diff2 = max2 - min1

    if diff1 > diff2:
        return diff1
    else:
        return diff2

# 4) https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/python
def count_red_beads(n):
    if n < 2:
        return 0
    return (n - 1) * 2


# 5) https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python
def missing_values(seq): 
    freq = {}
    for num in seq:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in freq:
        if freq[num] == 1:
            x = num
        if freq[num] == 2:
            y = num

    return x * x * y