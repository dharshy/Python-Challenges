__author__ = 'Priyadharshini'
def sort():
    inputdata = input()
    inputlist = inputdata.split(",")
    print(inputlist)
    inputlist.sort()
    return inputlist
sortedlist = sort()
print(",".join(sortedlist))
