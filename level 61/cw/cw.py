# 1)https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python
def get_average(marks):
    total = sum(marks)
    count = len(marks)
    return total // count
# 2)https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
def points(games):
    points = 0
    for i in games:
        x, y = i.split(":")
        x = int(x)
        y = int(y)
        
        if x > y:
            points += 3
        elif x == y:
            points += 1
            
    return points
# 3)https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
# 4)https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python
def number(bus_stops):
    total_people = 0  
    
    for stop in bus_stops:
        on, off = stop  
        total_people += on  
        total_people -= off 
    
    return total_people  
# 5)https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python
def generate_shape(n):
    shape = ""
    for i in range(n):
        shape += "+" * n + "\n"
    return shape[:-1]
# 6)https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
    if number < 0:
        return 0
    
    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:  
            total += i
    
    return total
# 7)https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 !=0:
            return num