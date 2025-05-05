# 2) https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
def dont_give_me_five(start,end):
    result = 0 
    for i in range(start, end + 1):
        if "5" not in str(i):
            result += 1
    return result

# 3) https://www.codewars.com/kata/525e5a1cb735154b320002c8/train/python
def triangular(n):
    if n <= 0:
        return 0
    else:
        return n * (n + 1) // 2

# 4) https://www.codewars.com/kata/580a4734d6df748060000045/train/python
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"

# 5) https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python
def bumps(road):
    if road.count("n") > 15:
        return "Car Dead"
    else:
        return "Woohoo!"