list=[4,5,6,7,2,9,3]
max=list[0]
sec_max=list[0]
third_max=list[0]
i=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i=i+1
i=0
while i<len(list):
    if list[i]>sec_max and list[i]!=max:
        sec_max=list[i]
    i=i+1
i=0
while i<len(list):
    if list[i]>third_max and list[i]!=sec_max and list[i]!=max:
        third_max=list[i]
    i=i+1
print(max)
print(sec_max)
print(third_max)
    

