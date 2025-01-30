# 1)გააგრძელეთ ამ ქოუდვარსების შესრულება და გააკეთეთ მინიმუმ 10  8 კიუანი ამოცანა

# https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd/train/python
def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m


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


# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
def find_average(numbers):
    if len(numbers) < 0:
        return 0
    else:
        return sum(numbers) / len(numbers)  #2 failed i dont get it?


# https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python
def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    elif p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    else:
        return "Draw!"