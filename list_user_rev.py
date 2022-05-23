# take user input and reverse the number
list=int(input("enter the number:"))
rev=str(list)
b=" "
i=-1
while i>=-len(rev):
    b=b+rev[i]
    i=i-1
print(b)


    
