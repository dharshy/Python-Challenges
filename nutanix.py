__author__ = 'Priyadharshini'

#f = open("test.txt")
filelist = f.readlines()
searchwords= input()
keylist =searchwords.split()
strpresent = False
count = 0
dict = {}
resultlist=[]
for key in keylist :
    for line in filelist:
        if key in filelist:
            #dictionary containing the search string and number of occurences
            dict[key] = count+1
            #list containing all the lines containing the keyword
            resultlist.append(line)
            break
    print(dict)
    print(resultlist)
