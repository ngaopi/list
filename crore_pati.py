list=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
a=0
b=0
c=0
while i<len(list):
    if list[i]>=10000000:
        a=a+1     
    elif list[i]>=100000:
        b=b+1
    elif list[i]<100000:
        c=c+1 
    i=i+1
print(a,"crore pati")
print(b,"lakh pati")
print(c,"dilwale")

    
        
