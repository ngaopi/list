list=[-5,-7,12,17,5,9,10,16,20,-17]
i=0
sum1=0
sum2=0
count1=0
count2=0
while i<len(list):
    if list[i]<0:
        sum1=sum1+list[i]
        count1+=1
    else:
        sum2=sum2+list[i]
        count2+=1
    i=i+1
print("negative sum =",sum1)
print("positive sum =",sum2)
print("count of even =",count1)
print("count of odd =",count2)