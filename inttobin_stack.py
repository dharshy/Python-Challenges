__author__ = 'Priyadharshini'
from stack import Stack
def inttobin(number,s):
    while number > 0:
        rem = number % 2
        print(rem)
        s.push(rem)
        number = number//2
        op = s.isEmpty()
        print(op)
    while True:
        if s.isEmpty():
            break
        else:
            result = s.pop()
            print(int(result))
if __name__ == "__main__":
    s=Stack()
    inttobin(233,s)
