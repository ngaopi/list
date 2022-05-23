list=['apple','banana','cherry','drynut']
i=0
c=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]==list[i][0]:
            b=list[i][0].upper()
            c.append(b)
            d=".".join(c)
        j=j+1
    i=i+1
print(d) 


              