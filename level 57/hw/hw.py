# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    else:
        return("green")

# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    result = []  
    for i in range(n):  
        result.append(x * (i + 1)) 
    return result

# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
def abbrev_name(name):
    first, last = name.split()
    return first[0].upper() + '.' + last[0].upper()

# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
    if not arr:  
        return []
    
    count_pos = 0
    sum_neg = 0
    
    for num in arr:
        if num > 0:
            count_pos += 1 
        elif num < 0:
            sum_neg += num
            
    return [count_pos, sum_neg]

# https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"