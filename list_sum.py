# write a python programme to sum all the item in the list
num=[1,2,3,4,5,6,7,8,9]
sum=0
i=num[0]
while i<=len(num):
    sum=sum+i
    print(sum)
    i=i+1
print("total sum is:",sum)
