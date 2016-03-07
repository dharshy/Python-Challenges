__author__ = 'Priyadharshini'
from queue import Queue
def hotpotato(namelist,num):
    for i in namelist:
        q.enqueue(i)
    print(q)
    if q.isEmpty() == False:
        while i < num:
            poppedelement = q.dequeue()
            q.enqueue(poppedelement)
        return q.dequeue()
if __name__ == "__main__":
    q = Queue()
    print("Enter the names for the hot-potato competition")
    names = input()
    namelist = names.split()
    print("Enter the number of passes")
    num = input()
    x = hotpotato(namelist,num)
    print(x)