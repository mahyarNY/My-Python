def anti_vowel(text):
    n = ""
    result = ""
    for i in range(len(text)):
        result = text.pop(i)
    return result 
    
print (anti_vowel("Hello"))
