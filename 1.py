def censor(text, word):
    text = text.replace(word, "*" * len(word))
    return text
print (censor("this is hack", "hack"))
