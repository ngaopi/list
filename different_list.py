# write a python program to get the difference between two list.
list1=[1,2,3,4,5,6,7,8,9]
list2=[2,5,3,10,45,32,78]
i=0
b=[]
while i<len(list1):
    if list1[i]not in list2:
        b.append(list1[i])
    i=i+1
j=0
c=[]
while j<len(list2):
    if list2[j]not in list1:
        c.append(list2[j])
    j=j+1
print("list 1 =",b)
print("list 2 =",c)
        

# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# b=[]
# while i<len(list1):
#     if list1[i]not in list2:
#         b.append(list1[i])
#     i=i+1
# print(b)
        

            
    
