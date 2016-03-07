__author__ = 'Priyadharshini'
def inputlist():
    lisinput = input()
    lisinput = lisinput.split()
    print(lisinput)
    return lisinput
def kthminelement(inputlis,n):
    sortedlist = sorted(inputlis)
    print(sortedlist)
    print(sortedlist[n-1])
if __name__ == "__main__":
    inputlis = inputlist()
    print("please enter the n value")
    n = input()
    kthminelement(inputlis,int(n))
