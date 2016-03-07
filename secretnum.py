__author__ = 'Priyadharshini'
import sys

def secretnum(x,low,high):
    mid = (low+high)/2
    if(low > high ) :return
    if mid == x: return x
    elif x < mid :
        secretnum(x,mid,high)
    elif x > mid:
        secretnum(x,mid+1, high)

if __name__ == "__main__":
    inputlist =[i for i in  range(1,100)]
    print(inputlist)
    x = input()
    low=inputlist[0]
    print(type(low))
    high = inputlist.pop()
    if x not in inputlist : print("Wrong entry")
    result = secretnum(int(x),int(low),int(high))
    print(result)