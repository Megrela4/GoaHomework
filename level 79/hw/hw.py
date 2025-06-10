# 1) https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
def solution(string):
    return string[::-1]

# 2) https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
def sum_array(a):
    total = 0
    for i in a:
        total += i
    return total

# 3) https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
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

