# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
def distinct(seq):
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    return result

# https://www.codewars.com/kata/515e188a311df01cba000003/train/python
def get_planet_name(id):
    if id == 1:
        return "Mercury"
    elif id == 2:
        return "Venus"
    elif id == 3:
        return "Earth"
    elif id == 4:
        return "Mars"
    elif id == 5:
        return "Jupiter"
    elif id == 6:
        return "Saturn"
    elif id == 7:
        return "Uranus"
    elif id == 8:
        return "Neptune"
    else:
        return ""

# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
def switch_it_up(number):
    if number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"
    else:
        return "Zero"