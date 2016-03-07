__author__ = 'Priyadharshini'
def bintoint():
    resultlist = []
    consoleinput = input()
    listinput = consoleinput.split(",")
    for num in listinput:
        intbin = int(num, 2)
        if intbin % 5 == 0:
            resultlist.append(num)
    return resultlist
result = bintoint()
print(result)