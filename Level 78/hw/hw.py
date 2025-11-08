# https://www.codewars.com/kata/57f6ad55cca6e045d2000627
def square_or_square_root(arr):
    result = []
    for num in arr:
        root = num ** 0.5  
        if root == int(root):  
            result.append(int(root))  
        else:
            result.append(num * num)  
    return result


# https://www.codewars.com/kata/57eaeb9578748ff92a000009
def sum_mix(arr):
    total = 0
    for i in arr:
        total += int(i)
    return total


# https://www.codewars.com/kata/57096af70dad013aa200007b
def logical_calc(array, op):
    if op == "AND":
        result = True
        for value in array:
            result = result and value
    elif op == "OR":
        result = False
        for value in array:
            result = result or value
    elif op == "XOR":
        result = False
        for value in array:
            result = result != value
    return result

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
def count_sheep(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " sheep..."
    return result