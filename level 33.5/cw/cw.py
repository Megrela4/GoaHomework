# 1)https://www.codewars.com/kata/5412509bd436bd33920011bc
# Credit Card Mask
# return masked string
def maskify(cc):
    st = ''
    l = []
    for i in cc[:-4]:
        l.append(i.replace(i,"#"))
    st += cc[-4:]
    return "".join(l) + st



# 2)https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
# String ends with?
def solution(text, ending):
    if text.endswith(ending):
        return True
    else:
        return False
    


