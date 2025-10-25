# Codewars No.1 :
# https://www.codewars.com/kata/5866fc43395d9138a7000006/train/python
def ensure_question(s):
        if s.endswith("?"):
            return s 
        else:
            return s + "?"


# Codewars No.2
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
def find_short(s):
    words = s.split()

    shortest = len(words[0])

    for i in words:
        if len(i) < shortest:
            shortest = len(i)
    return shortest


# Codewars No.3
# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    phone = "("
    for i in range(3):
        phone += str(n[i])
    phone += ") "
    for i in range(3, 6):
        phone += str(n[i])
    phone += "-"
    for i in range(6, 10):
        phone += str(n[i])
    return phone