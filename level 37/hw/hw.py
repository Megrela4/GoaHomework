# https://www.codewars.com/kata/570597e258b58f6edc00230d/train/python
def array(string):
    parts = string.split(',')
    if len(parts) <= 2:
        return None
    return ' '.join(parts[1:-1])


# https://www.codewars.com/kata/596fba44963025c878000039/train/python
def contamination(text, char):
    if text == "" or char == "":
        return ""
    return char * len(text)


# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]