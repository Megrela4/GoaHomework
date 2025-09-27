# 1) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# 2) https://www.codewars.com/kata/55edaba99da3a9c84000003b
def divisible_by(numbers, divisor):
    list =[]
    for i in numbers:
        if i % divisor == 0:
            list.append(i)
    
    return list

# 3) https://www.codewars.com/kata/55ecd718f46fba02e5000029
def between(a,b):
    return list(range(a, b + 1))

# 4) https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
def string_to_array(s):
    return s.split() if s else ['']



