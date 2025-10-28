# Codewars No.1
# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    s = str(n)
    digits = []
    
    for i in s:
        digits.append(int(i))
        
    digits.reverse()
    
    return digits

# Codewars No.2
# https://www.codewars.com/kata/59f11118a5e129e591000134/train/python
def repeats(arr):
    total = 0
    for i in arr:
        if arr.count(i) == 1:
            total += i
    return total

# Codewars No.3
# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
def remove_char(s):
    return s[1:-1]