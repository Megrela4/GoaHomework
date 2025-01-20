# https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
def sum_array(arr):
    if arr == None or arr == [] or len(arr) == 1:
        return 0
    else:
        return sum(arr) - min(arr) - max(arr)