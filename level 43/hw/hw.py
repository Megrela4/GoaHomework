# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python
def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        return sum(range(begin_number, end_number + 1, step))
    

# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result


# https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
def sum_mix(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total


# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python
def array_plus_array(arr1,arr2):
    total = 0
    
    for i in arr1:
        total += i

    for i in arr2:
        total += i

    return total


# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)