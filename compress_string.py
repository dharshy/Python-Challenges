__author__ = 'Priyadharshini'
# Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space
def compress_string(strinp = ""):
    #take inp and form a dict
    dict_input = {}
    count = 1
    for i in strinp:
        if i in dict_input:
            dict_input[i] += 1
        else:
            dict_input[i] = count
    #cannot change string - Immutable- so create a new string
    print(dict_input)
    newdict = {}
    for key,value in dict_input.items():
         if value > 2:
            oldstr = key*value
            newstr = key+ str(value)
            #this dict will contain the substrings that has to be replaced with alphanumeric strings
            newdict[oldstr] = newstr
            newstr = strinp.replace(oldstr,newstr)
            print(strinp)
    print(newdict)
    #from this dict we can form a new string- but this is not feasible as dictionaries are not ordered

if __name__ == "__main__":
    compress_string("AAABCCDDDD")


