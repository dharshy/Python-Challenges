__author__ = 'Priyadharshini'
class Queue():
    def __init__(self):
        self.count = 0
        self.quelist = []
    def enqueue(self,num):
        self.quelist.insert(0,num)
    def dequeue(self):
        return self.quelist.pop()
    def isEmpty(self):
        return self.quelist == []
    def size(self):
        for i in self.quelist:
            self.count += 1
    def __str__(self):
        return str(self.quelist)
