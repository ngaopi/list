list=[31,50,21,47,12,67,45]
i=0
while i<len(list):
    j=0
    while j<len(list)-1:
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        j=j+1
    i=i+1
print(list)
        
