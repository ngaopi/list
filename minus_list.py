list=[27,10,30,10,5,5]
i=0
b=[]
while i<len(list):
    j=list[i]-list[i+1]
    b.append(j)
    i=i+2
print(b)
