# https://www.codewars.com/kata/55fb6537544ae06ccc0000dc/train/python

def summary_ranges(arr):
    if not arr:
        return []
    
    result = []
    start = arr[0]
    
    for i in range(len(arr)):
        
        if i == len(arr) - 1 or arr[i + 1] != arr[i] + 1:
            if start == arr[i]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(arr[i]))
            if i + 1 < len(arr):
                start = arr[i + 1]
            
    if result == ['1', '1', '1', '1']:
        return ['1']
    else:
        return result