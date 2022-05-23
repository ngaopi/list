# num=[50,40,23,70,56,12,5,10,7]
# count=0
# while count<len(num):
#     print(count)
#     count=count+1

      
num=[1,3,5,7,9,4,12,8,6]
i=0
max=0
min=num[0]
while i<len(num):
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
    i=i+1
print("max no.is:",max)
print("min no.is:",min)




