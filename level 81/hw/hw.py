# 1) https://www.codewars.com/kata/529b418d533b76924600085d/train/python
def to_underscore(strng: str) -> str:
    if not isinstance(strng, str):
        return str(strng)
    
    result = ""
    for i, ch in enumerate(strng):
        if ch.isupper() and i != 0:
            result += "_"
        result += ch.lower()
    return result

# 2) https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python
def count_bits(n):
    count = 0
    while n > 0:
        if n % 2 == 1: 
            count += 1
        n = n // 2       
    return count

# 3) https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python
def kebabize(string):
    result = []
    for i in string:
        if i.isdigit():
            continue
        if i.isupper():
            if result:
                result.append('-')
            result.append(i.lower())
        else:
            result.append(i)
    return ''.join(result)

