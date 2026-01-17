# 1) https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    s = str(n)
    digits = []
    
    for i in s:
        digits.append(int(i))
        
    digits.reverse()
    
    return digits



