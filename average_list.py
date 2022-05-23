
list=[23,14,56,12,19,9,15,25,31,42,43]
length=len(list)
i=0
sum=0
sum1=0
while i<len(list):
    if list[i]%2==0:
        sum=sum+list[i]
        avg=sum//length
    else:
        sum1=sum1+list[i]
        avg1=sum1//length
    i=i+1
print("even sum =",sum)
print("even avg =",avg)
print("odd sum =",sum1)
print("odd avg =",avg1)





    