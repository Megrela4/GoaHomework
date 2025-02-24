# https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python
def derive(coefficient, exponent): 
    result = str(coefficient * exponent) + "x^" + str(exponent - 1)
    return result

# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python
def whatday(num):
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"

# https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
# https://www.codewars.com/kata/582dafb611d576b745000b74/train/python
def quote(fighter):
    if fighter.lower() == "george saint pierre":
        return "I am not impressed by your performance."
    elif fighter.lower() == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
