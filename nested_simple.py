list=[1,2,[3,4],[5,6],[12,3,45]]
i=0
b=[]
while i<len(list):
    if type(list[i])==type ([]):
        j=0
        while j<len(list[i]):
            b.append(list[i][j]) 
            j=j+1 
    else:
        b.append(list[i]) 
    i=i+1
print(b)