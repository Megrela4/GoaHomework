# 1) https://www.codewars.com/kata/52f3149496de55aded000410/train/python
def sum_digits(number):
    if number < 0:
        number = str(number).replace("-", "")
    else:
        number = str(number)
        
    result = 0
    
    for i in number:
        result += int(i)
        
    return result

# 2) https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python
def change(st):
    st = st.lower()
    result = ''
    
    for i in range(26):
        letter = chr(i + 97)
        if letter in st:
            result += '1'
        else:
            result += '0'
    
    return result

# 3) https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/python
def sort_gift_code(code):
    code_list = list(code)
    code_list.sort()
    sorted_code = ''.join(code_list)
    return sorted_code

# 4) https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
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