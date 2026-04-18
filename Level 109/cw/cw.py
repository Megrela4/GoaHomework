# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc


# https://www.codewars.com/kata/5aff237c578a14752d0035ae
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    sum = (
        age_1 * age_1 + age_2 * age_2 + age_3 * age_3 + age_4 * age_4 + age_5 * age_5 +
        age_6 * age_6 + age_7 * age_7 + age_8 * age_8
    )
    
    squareroot = sum ** 0.5
    
    return int(squareroot / 2)
    

# https://www.codewars.com/kata/58712dfa5c538b6fc7000569
def count_red_beads(n):
    if n < 2:
        return 0
    else:
        return (n - 1) * 2

# https://www.codewars.com/kata/58daa7617332e59593000006
def find_longest(arr):
    longest = arr[0]
    
    for i in arr:
        if len(str(i)) > len(str(longest)):
            longest = i
    return longest