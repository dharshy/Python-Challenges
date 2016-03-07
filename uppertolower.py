__author__ = 'Priyadharshini'
if __name__ =="__main__":
    s = "aBcD"
    a = []
    for char in s:
        if char.islower():
            a.append(char.upper())
        else:
            a.append(char.lower())
    print("".join(a))
    