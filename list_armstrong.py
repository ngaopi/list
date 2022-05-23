list=[153]
temp=list
i=0
sum=0
while list[i]>0:
    sum=sum+(list[i]%10)*(list[i]%10)*(list[i]%10)
    list=list//10
if temp==sum:
    print("armstrong")
else:
    print("not armstrong")





    