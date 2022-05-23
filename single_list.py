# list=[[3,4,5],[2],[4,8,9],[28,42]]
# i=0
# a=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         a.append(list[i][j])
#         j=j+1
#     i=i+1
# print(a)
                                                             
list=["aj","121","aba","243","abb","aa"]
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
   
            

        