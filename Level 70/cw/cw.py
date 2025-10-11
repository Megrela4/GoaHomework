# https://www.codewars.com/kata/557a2c136b19113912000010
def reverse_it(data):
    if type(data) == str:
        return data[::-1]
    elif type(data) == int or type(data) == float:
        s = str(data)[::-1]
        if "." in s:
            return float(s)
        else:
            return int(s)
    else:
        return data
    

# https://www.codewars.com/kata/55b42574ff091733d900002f
def friend(x):
    result = []
    for i in x:
        if len(i) == 4:
            result.append(i)
    return result


# https://www.codewars.com/kata/59a8570b570190d313000037
def sum_cubes(n):
      return sum(i ** 3 for i in range(1, n + 1))


# https://www.codewars.com/kata/55955a48a4e9c1a77500005a
def greet(name):
    if name:
        return f"hello {name}!"
    else:
        return None
    

# https://www.codewars.com/kata/54da5a58ea159efa38000836
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 !=0:
            return num
