def censor(text, exam):
    astriks = []
    for i in range(len(exam)):
        astriks.append("*")
    astriks = "".join(astriks)
    words = text.split(" ")
##    for word in words:
##        if word == exam:
            
    return astriks
print (censor("this hack is wack hack", "hack"))
