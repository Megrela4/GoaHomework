# 1) https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/train/python
def past(h, m, s):
    return (h * 3600 + m * 60 + s) * 1000

# 2) https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python
def find_needle(haystack):
    position = haystack.index("needle")
    return f"found the needle at position {position}"

# 3) https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result

# 4) https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python
def rental_car_cost(d):
    cost = 40
    total = d * cost
    
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20
        
    return total

# 5) https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def is_triangle(a, b, c):
    if  a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# 6) https://www.codewars.com/kata/57f609022f4d534f05000024/train/python
def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
        
# 7) https://www.codewars.com/kata/59f11118a5e129e591000134/train/python
def repeats(arr):
    total = 0
    for i in arr:
        if arr.count(i) == 1:
            total += i
    return total
