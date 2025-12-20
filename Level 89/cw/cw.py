# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python

def dashatize(n):
    if n is None:
        return "None"
    
    num = str(n)
    if num[0] == "-":
        num = num[1:]
        
    result = []
    
    for i in num:
        if int(i) % 2 == 1:
            if result and result[-1] != "-":
                result.append("-")
            result.append(i)
            result.append("-")
        else:
            result.append(i)

    return "".join(result).strip("-")