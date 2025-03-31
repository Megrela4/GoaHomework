#https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
def count_positives_sum_negatives(arr):
    if not arr:  
        return []
    
    count_pos = 0
    sum_neg = 0
    
    for num in arr:
        if num > 0:
            count_pos += 1 
        elif num < 0:
            sum_neg += num
            
    return [count_pos, sum_neg]


#https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
def are_you_playing_banjo(name):
    if name[0] == "r":
        return name + " plays banjo"
    
    elif name[0] == "R":
        return name + " plays banjo"
    
    else:
        return name + " does not play banjo"
    

#https://www.codewars.com/kata/583710ccaa6717322c000105/train/python
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    elif number % 2 >= 1:
        return number * 9


#https://www.codewars.com/kata/57f780909f7e8e3183000078/train/python
def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result


#https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    
    result = ""
    
    for i in string_:
        if i not in vowels:
            result += i
    return result
