__author__ = 'Priyadharshini'
def lettersdigit():
    dictinp ={"digits":0,"alpha":0}

    letter=0
    consoleinput = "qwe123"
    for i in consoleinput:
        if i.isdigit():
            dictinp["digits"] = dictinp["digits"] + 1
        elif i.isalpha():
            dictinp["alpha"] = dictinp["alpha"] + 1
    return dictinp
s = lettersdigit()
print(s)