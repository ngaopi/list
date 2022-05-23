#13. write a python program to print the numbers of a specified list after 
#    removing even numbers.
list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    if list[i]%2==0:
        list.pop(i)
    i=i+1
print(list)

