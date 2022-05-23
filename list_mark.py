# suppose we have a list of marks and we have to find how many students have mark
# less than 50. 
mark=[45,23,89,76,65,90,54,23,76]
length=len(mark)
more_50=0
less_50=0
i=0
while i<len(mark):
    if mark[i]<50:
        less_50+=1
    else:
        more_50+=1
    i=i+1
print("marks more than 50 =",more_50)
print("marks less than 50 =",less_50)