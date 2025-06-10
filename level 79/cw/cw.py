# 1) https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python
def small_enough(array, limit):
    for num in array:
        if num > limit:
            return False
    return True

# 2) https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python
def largest_pair_sum(numbers): 
    numbers.sort()
    return numbers[-1] + numbers[-2]

# 3) https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    words = sentence.split() 
    result = []  
    
    for word in words:
        if len(word) >= 5:  
            new_word = ""  
            for i in word:
                new_word = i + new_word  
            result.append(new_word)
        else:
            result.append(word)  
    
    return " ".join(result)

# 5) https://www.codewars.com/kata/50654ddff44f800200000004/train/javascript
# function multiply(a, b) {
#   return a * b;
# }

# 6) https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/javascript
# function evenOrOdd(number) {
#   if (number % 2 === 0) {
#     return "Even";
#   } else {
#     return "Odd";
#   }
# }

# 7) https://www.codewars.com/kata/55685cd7ad70877c23000102/train/javascript
# function makeNegative(num) {
#   if (num > 0) {
#     return -num;
#   } else {
#     return num;
#   }
# }

# 8) https://www.codewars.com/kata/56dec885c54a926dcd001095/train/javascript
# function opposite(number) {
#   return -number;
# }