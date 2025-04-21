# 1) https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)

# 2) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# 3) https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
def accum(st):
    result = []
    for i in range(len(st)):
        char = st[i]
        part = char.upper() + char.lower() * i
        result.append(part)
    return '-'.join(result)

# 4) https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    if not pin.isdigit():
        return False
    
    if len(pin) == 4 or len(pin) == 6:
        return True
    else:
        return False

# 5) https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
def row_sum_odd_numbers(n):
    result = n * n * n
    return result