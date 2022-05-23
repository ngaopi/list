mark=[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]

# i=0
# j=0
# k=0
# sum0=0
# sum1=0
# sum2=0
# while i<len(mark[2]):
#     sum0=sum0+mark2[i]
#     i=i+1
# print("mark2 sum is:",sum0)
# while j<len(mark[1]):
#     sum1=sum1+mark1[j]
#     j=j+1
# print("mark1 sum is:",sum1)
# while k<len(mark[0]):
#     sum2=sum2+mark0[k]
#     k=k+1
# print("mark0 sum is:",sum2)
# print(sum0+sum1+sum2)
i=0
sum=0
while i<len(mark):
    j=0
    while j<len(mark[i]): 
        sum=sum+mark[i][j]
        j=j+1
    i=i+1
print(sum)