#https://www.codewars.com/kata/559590633066759614000063/train/python
def min_max(lst):
    return [min(lst), max(lst)]


#https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


#https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
