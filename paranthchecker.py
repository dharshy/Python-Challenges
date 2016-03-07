__author__ = 'Priyadharshini'
from stack import Stack

def checker(symbolstring,s):
    for i in symbolstring:
        if i in "({[":
            s.push(i)
            print(s)
        else:
            if s.isEmpty():
                print("unbalanced paranthesis")
                return
            else:
                s.pop()
                print(s)
    if s.isEmpty()  == True:
        print("Paranthesis balanced")
    else:
        print("Paranthesis not balanced")
if __name__ == "__main__":
    s = Stack()
    inputsym = "{}}({)"
    checker(inputsym,s)