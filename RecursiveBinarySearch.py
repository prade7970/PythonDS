
def recursivebinarysearch(lst,target):
    if(len(lst))==0:
        return False
    else:
        midpoint =len(lst)//2
        if lst[midpoint]==target:
            return True
        else:
            if lst[midpoint]<target:
                return recursivebinarysearch(lst[midpoint+1:], target)
            else:
                if lst[midpoint]>target:
                    return recursivebinarysearch(lst[:midpoint], target)

#def verify(result):
#    print("Target Found",result)

lst=[1,2,3,4,5,6]
target=5

d=recursivebinarysearch(lst, target)
print(d)