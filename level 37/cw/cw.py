# https://www.codewars.com/kata/56a946cd7bd95ccab2000055/train/python
def lowercase_count(strng):
    count = 0
    for i in strng:
        if i.islower():
            count += 1
    return count


# https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python
def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result