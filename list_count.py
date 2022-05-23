# write a code that counts the numbers between 20 and 40 and then print its count.
list=[50,40,32,43,56,78,5,10,12,17,7] 
# i=0
# count=0
# while i<len(list):
#     if list[i]>=20 and list[i]<=40:
#         count=count+1
#     i=i+1
# print(count)


list=['aba','123','111','kic','tart','pip']
i=0
count=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][0]==list[i][-1]:
            count=count+1
            break
        j=j+1
    i=i+1
print(count)
        

            