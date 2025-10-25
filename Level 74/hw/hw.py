# Codewars 8 kuy:
# 1) https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python
def validate_hello(greetings):
    hellos = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc', 'hej', 'hei', 'hoi']
    greetings = greetings.lower()
    
    for word in hellos:
        if word in greetings:
            return True
    return False

# 2) https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python
def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"


# 4) https://www.codewars.com/kata/59441520102eaa25260000bf/train/python
def unusual_five():
    return len("five!")


# Codewars 7kyu:

# 1) https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
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

# 2) https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# 3) https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
def DNA_strand(dna):
    result = ""
    for letter in dna:
        if letter == 'A':
            result += 'T'
        elif letter == 'T':
            result += 'A'
        elif letter == 'C':
            result += 'G'
        elif letter == 'G':
            result += 'C'
    return result


# Codewars 6 kuy:

# 1) https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 !=0:
            return num