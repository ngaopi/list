#18 write a python program to generate all premutations of a list in python.

list=["love","you",-63,78,87.2,-21,45,90.1]
i=0
a=[]
b=[]
c=[]
d=[]
while i<len(list):
    if (type(list[i])==str):
        a.append(list[i])
    elif (type(list[i])==float):
        b.append(list[i])
    elif list[i]>0:
        c.append(list[i])
    else:
        d.append(list[i])
    i=i+1
print(a,"\n",b,"\n",c,"\n",d) 