# list=[1,2,3,5,6,7,8,9]
# list1=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(list1):
#     if list1[i]not in list:
#         print("false")
#     else:
#         print("true")
#     i=i+1
    
# take out the duplicates from the list and put in different list and print it
list=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
a=[]
while i<len(list):
    if list[i]not in a:
        a.append(list[i])
    i=i+1
print(a)


