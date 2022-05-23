# write a python programme to print the maximum number from a list.
a=['simplicity', 'is', 'better','complex']
i=0
max=0
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
    i=i+1
print(max)

