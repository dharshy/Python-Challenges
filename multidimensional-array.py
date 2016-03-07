__author__ = 'Priyadharshini'
def multilist():
    inputlist = [[]]
    consoleinput = input()
    listinp = [int(x) for x in consoleinput.split(",")]
    print(listinp)
    rownum = listinp[0]
    colnum= listinp[1]
    inputlist = [[0 for col in range(colnum)]for i in range(rownum)]
    for i in range(rownum):
        for x in range(colnum):
                inputlist[i][x] = i*x
    return inputlist
outputlist = multilist()
print(outputlist)
