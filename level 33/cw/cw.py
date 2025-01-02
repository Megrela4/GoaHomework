# https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python
# Volume of a Cuboid
def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    return length * width * height


# https://www.codewars.com/kata/55d277882e139d0b6000005d/train/python
# Grasshopper - Array Mean
def find_average(nums):
    #your code here
    sum = 0
    for i in nums:
        sum += i
    return sum / len(nums)


# https://www.codewars.com/kata/570a6a46455d08ff8d001002/train/python
# No zeros for heros
def no_boring_zeros(n):
    # your code
    if n == 0:
        return 0
    
    n = str(n)
    
    while n[-1] == "0":
        n= n[:-1]
        
    return int(n)



# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
# Exes and Ohs
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


# https://www.codewars.com/kata/59ca8246d751df55cc00014c/train/python
# Is he gonna survive?
def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False
    