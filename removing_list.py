#12. write a python program to print a specified list after removing the 0th,
#    4th and 5th elements.
# list=['red','green','white','black','yellow','pink','blue']

#     if i==0 or i==4 or i==5 or i==6:
#         list.pop(i)
#     i+=1
# print(list)

list=[1,3,2]
i=0
b=""
while i<len(list):
    j=i+1
    while j<len(list):
        k=list[j]-list[i]
        b+=str(k)+","
        j+=1
    i+=1
k=b[0:3]
print(k)        