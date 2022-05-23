#11. write a python function that take two list and returns true if they have 
#     tleast one common member
list1=['apple','banana','grapes']
list2=['litchi','guava','grapes']
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        if list1[i]==list2[j]:
            print("true")
        else:
            print("false")
        j+=1
    i=i+1
