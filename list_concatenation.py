# concatenation of two items in list
list=[1,2,3,4,5,6,7,8]
i=0
k=[]
while i<len(list):
    j=list[i],list[i+1]
    k.append(j)
    i=i+2
print(k)
    