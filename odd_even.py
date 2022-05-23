# write a code that works for any list, and that tells how many odd numbers and 
# how many even numbers are there in the given list.
list=[23,14,56,12,19,9,15,25,31,42,43]
i=0
j=0
count=0
count1=0
while i<len(list):
    if list[i]%2==0:
        count=count+1
    i=i+1
print("even =",count)
while j<len(list):
    if list[j]%2!=0:
        count1=count1+1
    j=j+1
print("odd =",count1)

        


   
   



