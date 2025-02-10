# https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python
def format_money(amount):
    return f"${amount:.2f}"


# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python
def same_case(a, b): 
    if a.isalpha() == False or b.isalpha() == False:
        return -1
    
    elif a.islower() == True and b.islower() == True:
        return 1
    
    elif a.isupper() == True and b.isupper() == True:
        return 1
    else:
        return 0
    
    
# https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python
def sum_mul(n, m):
    if m <= 0 or n <=0:
        return "INVALID"
    
    
    total = 0
    for i in range(n, m, n):
        total += i
        
    return total


# https://www.codewars.com/kata/5761a717780f8950ce001473/train/python
def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    
    if age > 0:

        if age == 1:
            return f"You are {age} year old."
        else:
            return f"You are {age} years old."
    elif age < 0:
        
        if age == -1:
            return f"You will be born in {-age} year."
        else:
            return f"You will be born in {-age} years."
    else:
        return "You were born this very year!"

