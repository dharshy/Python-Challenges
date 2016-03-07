__author__ = 'Priyadharshini'
#Determine if a string is a permutation of another string¶
import sys
import string
def permutation(str1,str2):
    #it shouldn't be a palindrome -MOM \
    #nib -bin -->false
    #act - cat -->True
    #c at - a ct -->True
    #sort both of the strings
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)
    if sort_str1 == sort_str2:
        print("They are permutations of each other")
    else:
        print("not permutations of each other")

permutation("act","cat")
permutation("bin","nib")