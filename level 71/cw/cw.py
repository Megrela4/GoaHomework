# 1) https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result

# 2) https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    word = word.lower()
    result = ""
    for i in word:
        if word.count(i) == 1:
            result += "("
        else:
            result += ")"
    return result

# 3) https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
def solution(s):
    result = ""
    for i in s:
        if i.isupper():
            result += " " + i
        else:
            result += i
    return result

# 4) https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python
def in_asc_order(arr):
    return arr == sorted(arr)

# 5) https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python
def remove_duplicate_words(s):
    words = s.split()
    result = []
    for i in words:
        if i not in result:
            result.append(i)
    return " ".join(result)