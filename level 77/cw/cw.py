# 1) https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b

# 2) https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    return sorted(test) == sorted(original)

# 3) https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    result = []  
    for i in range(n):  
        result.append(x * (i + 1)) 
    return result

# 4) https://www.codewars.com/kata/5a023c426975981341000014/train/python
def other_angle(a, b):
    return 180 - a - b

# 5) https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3/train/python
def sum_even_numbers(seq): 
    total = 0
    for i in seq:
        if i % 2 == 0:
            total += i
    return total
