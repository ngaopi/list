list=[1,34,11,3,9,6,2,13]
i=0
a=[]
while i<len(list):
    if list[i]==11:
        a.append(list[i])
    elif list[i]==13:
        a.append(list[i])
    i=i+1
print(a)