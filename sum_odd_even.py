# write a code that should give two sums as outputs , one is the sum of odd numbers
# present in all the list and the other is the sum of even numbers present in list.
list=[23,14,56,12,19,9,15,25]
i=0
j=0
sum1=0
sum2=0
avg=0
while i<len(list):
    if list[i]%2==0:
        sum1+=list[i]
        avg0=sum1//3
    i=i+1
print("even =",sum1)
print("even avg =",avg0)
while j<len(list):
    if list[j]%2!=0:
        sum2+=list[j]
        avg1=sum2//4
    j=j+1
print("odd =",sum2)
print("odd avg =",avg1)



