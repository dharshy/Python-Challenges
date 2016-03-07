__author__ = 'Priyadharshini'
#Dequeue DS can insert at front and rear
class Dequeue():
    def __init__(self):
        self.dqlist = []
        self.count = 0
    def insertRear(self,x):
        self.dqlist.insert(0,x)
    def insertFront(self,x):
        self.dqlist.append(x)
    def removeRear(self):
        return self.dqlist.pop(0)
    def removeFront(self):
        return self.dqlist.pop()
    def isEmpty(self):
        return self.dqlist == []
    def size(self):
        for i in self.dqlist:
            self.count = self.count+1
            return self.count
    def __str__(self):
        return str(self.dqlist)



