# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += alphabet.upper()
    start = alphabet.index(chars[0])
    
    i = 0
    while i < len(chars):
        if alphabet[start + i] != chars[i]:
            return alphabet[start + i]
        i += 1


# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
def likes(names):
    n = len(names)
    
    if n == 0:
        return "no one likes this"
    if n == 1:
        return f"{names[0]} likes this"
    if n == 2:
        return f"{names[0]} and {names[1]} like this"
    if n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    return f"{names[0]}, {names[1]} and {n-2} others like this"


# https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python
def kebabize(st):
    result = []
    for i in st:
        if i.isdigit():
            continue
        if i.isupper():
            if result:
                result.append('-')
            result.append(i.lower())
        else:
            result.append(i)
    return ''.join(result)