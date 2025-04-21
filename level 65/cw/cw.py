# 2) https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python
def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + ". " + animals[i] + "\n"
    return list

# 3) https://www.codewars.com/kata/59811fd8a070625d4c000013/train/python
def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent
    return str(new_coefficient) + "x^" + str(new_exponent)

# 4) https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python
def break_chocolate(n, m):
    if n == 0 or m == 0:
        return 0
    return n * m -1

# 5) https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    return sorted(test) == sorted(original)

# 6) https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python
def in_asc_order(arr):
    return arr == sorted(arr)

# 7) https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python
def flatten_and_sort(array):
    flattened = []
    for sublist in array:
        for item in sublist:
            flattened.append(item)
    return sorted(flattened)
