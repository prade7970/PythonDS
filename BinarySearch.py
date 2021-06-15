"""
Program illustrates binary search (needs sorted array)
O(log(n)) time complexity
test
"""

def binarysearch(lst,target):
    first=0
    last= len(lst)-1

    while first <= last:
        midpoint= (first+last)//2

        if lst[midpoint]==target:
            return midpoint
        elif lst[midpoint]< target:
            first=midpoint+1
        else:
            last=midpoint-1
    return -1


lst=[1,2,3,4,5,6]
target=5

d=binarysearch(lst, target)
print(d)



