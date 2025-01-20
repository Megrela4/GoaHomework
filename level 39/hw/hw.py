# გააკეთეთ მინიმუმ 5 ქოუდვარსი მოცემული კოლექციიდან
# https://www.codewars.com/kata/search/python?q=&r%5B%5D=-8&xids=completed&beta=false&order_by=total_completed%20desc






# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
def number_to_string(num):
    return str(num)


# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
def positive_sum(arr):
    total = 0
    for i in arr:
        if i >= 0:
            total += i
    return total


# https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/python
def sum_array(a):
    total = 0
    for i in a:
        total += i
    return total


# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python
def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return  "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    

# https://www.codewars.com/kata/577a98a6ae28071780000989/train/python
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)
    

