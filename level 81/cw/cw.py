# 1) https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python
def problem(a):
    if type(a) == str:
        return "Error"
    else:
        return a * 50 + 6

# 3) https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/python
def flick_switch(lst):
    result = []
    switch = True
    
    for i in lst:
        if i == "flick":
            switch = not switch
        result.append(switch)
    
    return result

# 4) https://www.codewars.com/kata/570669d8cb7293a2d1001473/train/python
def if_chuck_says_so():
    return 0

# 5) https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(lst):
    result = []
    zero_count = 0
    
    for i in lst:
        if i == 0:
            zero_count += 1
        else:
            result.append(i)
    
    for i in range(zero_count):
        result.append(0)
        
    return result

# 6) https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
def pig_it(text):
    words = text.split()
    result = []
    
    for i in words:
        if i.isalpha():
            new_word = i[1:] + i[0] + "ay"
            result.append(new_word)
        else:
            result.append(i)
            
    return " ".join(result)

# 7) https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
def domain_name(url):
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    
    if url.startswith("www."):
        url = url[4:]
    
    return url.split(".")[0]

# 8) https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/python
def alphanumeric(password):
    return password.isalnum()