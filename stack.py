__author__ = 'Priyadharshini'
class Stack():
    def __init__(self):
        self.stacklist = []
    #should not print within this method just return the value that
    #needs to be printed.if the return value is not of type str
    #typecast to str and return it
    def __str__(self):
        return str(self.stacklist)
    def push(self,x):
        self.stacklist.append(x)
    def pop(self):
        self.stacklist.pop()
    def isEmpty(self):
        return self.stacklist == []
    def peek(self):
        return self.stacklist[len(stacklist)-1]
    def size(self):
        count = 0
        for i in self.stacklist:
            count += 1
        print(count)
