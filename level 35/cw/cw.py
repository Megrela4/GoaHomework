# https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python
def max_multiple(divisor, bound):
    result = []
    
    for i in range(1, bound + 1):
        if i % divisor == 0:
            result.append(i)
            
    return max(result)
    

# https://www.codewars.com/kata/52f3149496de55aded000410/train/python
def sum_digits(number):
    if number < 0:
        number = str(number).replace("-", "")
    else:
        number = str(number)
        
    result = 0
    
    for i in number:
        result += int(i)
        
    return result


# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
def sum_array(arr):
    if arr == None or arr == [] or len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)