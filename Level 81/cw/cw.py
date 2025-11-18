# https://www.codewars.com/kata/557a2c136b19113912000010/train/python
def reverse_it(data):
    if type(data) == str:
        return data[::-1]
    elif type(data) == int or type(data) == float:
        s = str(data)[::-1]
        if "." in s:
            return float(s)
        else:
            return int(s)
    else:
        return data
    
# https://www.codewars.com/kata/56d02e6cc6c8b49c510005bb/train/python
def find_missing_numbers(arr):
    if not arr:
        return []
    
    result = []
    start = min(arr)
    end = max(arr)
    
    for i in range(start, end + 1):
        if i not in arr:
            result.append(i)
            
    return result

# https://www.codewars.com/kata/5a1dc4baffe75f270200006b/train/python
def only_duplicates(st):
    result = ""
    for i in st:
        if st.count(i) > 1:
            result += i
    return result

