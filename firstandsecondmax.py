__author__ = 'Priyadharshini'
class maxnextmax():
    resultlist =[]
    def firstsecondmax(self,inputlist):
        #print("******I/P list*****")
        #print(inputlist)
        if len(self.resultlist) == 2: return
        maxelement = inputlist[0]
        for i in inputlist:
            if i > maxelement:
                maxelement = i
        self.resultlist.append(maxelement)
        #print("*****Resultlist*****")
        #print(self.resultlist)
        inputlist.remove(maxelement)
        self.firstsecondmax(inputlist)
        return self.resultlist


obj = maxnextmax()
inputlist = [1,2,3,4,5,6,7,8]
result = obj.firstsecondmax(inputlist)
print(result)