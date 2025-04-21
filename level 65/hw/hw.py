# 1) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    result = []
    for i in l:
        if type(i)== int:
            result.append(i)
    return result

# 2) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# 3) https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

