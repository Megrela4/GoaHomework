# 1)https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
def solution(string):
    return string[::-1]

# 2)https://www.codewars.com/kata/56dae9dc54c0acd29d00109a/train/python
def main (verb, noun):
    return verb + noun

# 3)https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l + w)
    
# 4)https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
def make_negative( number ):
    return -abs(number)

# 5)https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python
def accum(st):
    result = []
    for i in range(len(st)):
        char = st[i]
        part = char.upper() + char.lower() * i
        result.append(part)
    return '-'.join(result)

# 7)https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    return sorted(test) == sorted(original)
