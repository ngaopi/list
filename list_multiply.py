# write a python programme to multiply all the items in the list
num=[1,2,3,4,5,6,7,8,9]
i=0
sum=1 
while i<len(num):
    sum=sum*num[i]  
    i=i+1
    print(sum)
print("multiplication of all the no.is:",sum)
