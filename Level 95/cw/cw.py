# https://www.codewars.com/kata/515f51d438015969f7000013/train/python
def pyramid(n):
    if n < 1:
        return []
    pyramid = []
    for i in range(1, n + 1):
        pyramid.append([1] * i)
    return pyramid


# https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python
def triple_double(num1, num2):
    str1 = str(num1)
    str2 = str(num2)
    
    for i in "0123456789":
        if i * 3 in str1 and i * 2 in str2:
            return 1
    return 0


# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
def clean_string(s):
    result = []
    
    for i in s:
        if i == "#":
            if result:
                result.pop()
        else:
            result.append(i)
    return "".join(result)


# https://www.codewars.com/kata/59325dc15dbb44b2440000af/train/python
def is_alt(s):
    vowels = "aeiouAEIOU"
    
    for i in range(1, len(s)):
        if (s[i] in vowels and s[i-1] in vowels) or (s[i] not in vowels and s[i-1] not in vowels):
            return False
    return True