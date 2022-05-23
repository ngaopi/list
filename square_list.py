# 16. write a python program to generate and print a list of first and last five 
#     element where the value are square of numbers between 1 and 30(both includes).
# list=['2','3','4','5','6']
# b=[]
# i=1
# while i<len(list):
#     k=list[i-1]+','+list[i]
#     b.append([k])
#     i=i+2
# print(b)
    
list=457
a=str(list)
i=0
while i<len(a):
    print(int(a[i])**2,end=" ")
    i=i+1    
    