__author__ = 'Priyadharshini'
#application of Dequeue to check a palindrome
from dequeue import Dequeue
def palchecker(palstring,q):
    for element in palstring:
        q.insertRear(element)
        palflag = True
    while q.size()>1 and palflag is True:
        if q.removeFront() == q.removeRear():
            continue
        else :
            palflag = False
    return palflag

if __name__ == "__main__":
    q = Dequeue()
    result = palchecker("radar",q)
    if result == True : print("palindrome")
    else : print("not a palindrome")
