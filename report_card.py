# these are the marks of any students for the last three years.you have to calculate
# total marks of all the three years
list=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
# i=0
# j=0
# k=0
# sum0=0
# sum1=0
# sum2=0
# while i<len(list[0]):
#     sum0=sum0+list[0][i]
#     i=i+1
# while j<len(list[1]):
#     sum1=sum1+list[1][j]
#     j=j+1
# while k<len(list[2]):
#     sum2=sum2+list[2][k]
#     k=k+1
# print("total mark =",sum0+sum1+sum2)

i=0
sum=0
while i<len(list):
    j=0
    while j<len(list[i]):
        sum=sum+list[i][j]
        j=j+1
    i=i+1
print(sum)
        
        
                       