# write a python to remove duplicates from a list.

list=[2,3,4,5,2,3,4,5,6,7,8,6,5,6]
i=0
a=[]
while i<len(list):
    if list[i]not in a:
        a.append(list[i])
    i=i+1
print(a)


        

