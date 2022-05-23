mark=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
j=0
k=0
sum0=0
sum1=0
sum2=0
while i<len(mark[0]):
    sum0=sum0+mark[0][i]
    avg0=sum0//5
    i=i+1
print("total =",sum0)
print("1st yr avg =",avg0)
while j<len(mark[1]):
    sum1=sum1+mark[1][j]
    avg1=sum1//5
    j=j+1
print("total =",sum1)
print("2nd yr avg =",avg1)
while k<len(mark[2]):
    sum2=sum2+mark[2][k]
    avg2=sum2//5
    k=k+1
print("total =",sum2)
print("3rd yr avg =",avg2)
