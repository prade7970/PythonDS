def LinearSearch(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return -1



list=[1,2,3,4,5]
target=3

d= LinearSearch(list, target)
print(d)
