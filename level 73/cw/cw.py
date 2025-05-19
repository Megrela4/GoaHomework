# 1) https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python
def printer_error(s):
    errors = 0
    total = 0
    
    for letter in s:
        total = total + 1
        if letter < 'a' or letter > 'm':
            errors = errors + 1
    
    result = str(errors) + "/" + str(total)
    return result

# 2) https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
def number(bus_stops):
    total_people = 0  
    
    for stop in bus_stops:
        on, off = stop  
        total_people += on  
        total_people -= off 
    
    return total_people

# 3) https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
def dont_give_me_five(start,end):
    result = 0 
    for i in range(start, end + 1):
        if "5" not in str(i):
            result += 1
    return result

# 4) https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result

# 5) https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk):
    steps = 0
    x = 0
    y = 0

    for direction in walk:
        steps = steps + 1

        if direction == 'n':
            y = y + 1
        if direction == 's':
            y = y - 1
        if direction == 'e':
            x = x + 1
        if direction == 'w':
            x = x - 1

    if steps == 10 and x == 0 and y == 0:
        return True
    else:
        return False

# 6) https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    while True:
        num = n
        total = 0

        while num > 0:
            digit = num - (num // 10) * 10
            total = total + digit
            num = num // 10

        if total < 10:
            return total
        else:
            n = total

# 7) https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(sequence):
    result = []
    index = 0

    for item in sequence:
        if index == 0:
            result.append(item)
            index = index + 1
        else:
            last = result[index - 1]
            if item != last:
                result.append(item)
                index = index + 1

    return result