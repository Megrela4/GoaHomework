# 1)https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    result = []
    for i in l:
        if type(i)== int:
            result.append(i)
    return result
# 2)https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
def xo(s):
    s = s.lower()
    x = 0
    o = 0
    
    for i in s:
        if i == "x":
            x += 1
        elif i == "o":
            o += 1
    return x == o
# 3)https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

# 4)https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

# 5)https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python