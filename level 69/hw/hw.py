# 1) https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
def create_phone_number(n):
    part1 = f"({n[0]}{n[1]}{n[2]})"
    part2 = f" {n[3]}{n[4]}{n[5]}"
    part3 = f"-{n[6]}{n[7]}{n[8]}{n[9]}"
    return part1 + part2 + part3

# 2) https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 !=0:
            return num


# 3) https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result

# 4) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]