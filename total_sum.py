# how to find pairs in array if integers whose sum is equal to the given number.
list=[10,11,12,13,14,17,18,19]
n=len(list)
sum=30
i=0
while i<n:
    j=0
    while j<n:
        if (list[i]+list[j]==sum):
            print([list[i],list[j]],end=" ")
        j=j+1
    i=i+1



    


    


        

    
    
    
    
    
    
    
    
  