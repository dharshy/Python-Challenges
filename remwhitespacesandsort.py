__author__ = 'Priyadharshini'
def remwhitesort():
    resultlist = []
    consoleinput = input()
    listinput = consoleinput.split(" ")
    print(listinput)
    for word in listinput:
        if word not in resultlist:
            resultlist.append(word)
    return sorted(resultlist)
result = remwhitesort()
lineresult = " ".join(result)
print(lineresult)



