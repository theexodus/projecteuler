#! /usr/bin/python3

def natNum(val):
    vals=[]
    total=0
    for num in range(1,val):
        if num%3==0:
            vals.append(num)
        elif num%5==0:
            vals.append(num)
    for aVal in vals:
        total+=aVal
    print(total)
    return total
