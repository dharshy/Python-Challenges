__author__ = 'Priyadharshini'
# Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring¶
def is_substr(str2,strinp):
    if str2 in strinp:
        return True
#Logic is to add str1 +str1 and see if str2 is a substring
#if str2 is a substring of str1+str1 then these are rotational strings
def rotation(str1,str2):
    strinp = str1+str1
    print(strinp)
    result = is_substr(str2,strinp)
    if result == True:
        print("Rotational String")

if __name__ == "__main__":
    rotation("abc","bca")