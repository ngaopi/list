list="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr="over"
rep="on"
str=list.split()
i=0
while i<len(str):
    if str[i]==substr:
        del str[i]
    else:
        print(str[i],end=" ")
    i=i+1
a=list.replace(substr,rep)
print(a)

