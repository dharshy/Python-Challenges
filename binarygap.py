__author__ = 'Priyadharshini'
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(n):
    int_to_bin = bin(n)
    print(int_to_bin)
    if len(str(n))< 0: return
    if '0' in int_to_bin is False:
        return
    for i in int_to_bin:
        count =0
        flag = 'nothing'
        zero = 0
        zerocount = 0
        if i == 1 and count == 0:
            #substr.append(i)
            count = 1
            flag = 'start'
        if i == 0 and count == 1:
            #substr.append(i)
            zero = zero +1
        if i == 0 and count ==0:
            pass
        if i ==1 and count ==1:
            substr.append(i)
            i = i-1
            count = 0
            flag = 'end'
        if flag is 'end':
            if zerconunt > zero:
              zerocount = zero
            else:
              zerocount = zero
        print(zerocount)

solution(5)


