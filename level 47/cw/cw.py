# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python
def expression_matter(a, b, c):
    return max(
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c)
    )

# https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python
def dup(arry):
    result = []
    
    for word in arry:
        new_word = ""
        prev_i = None  
        
        for i in word:
            if i != prev_i: 
                new_word += i
            prev_i = i  
        
        result.append(new_word)
    
    return result

# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    words = sentence.split() 
    result = []  #
    
    for word in words:
        if len(word) >= 5:  
            new_word = ""  
            for i in word:
                new_word = i + new_word  
            result.append(new_word)
        else:
            result.append(word)  
    
    return " ".join(result)

