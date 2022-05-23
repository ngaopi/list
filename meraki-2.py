# suppose we have a list of marks and we have to find that how many students have marks 
# less than  50.For doing this write the code given below.
student_marks=[23,45,67,89,90,54,34,21,34,23]
list_length=len(student_marks)
index=0
less_than_50=0
more_than_50=0
while index< list_length:
    marks=student_marks[index]
    if marks<50:
        less_than_50=less_than_50+1
    else:
        more_than_50=more_than_50+1
    index=index+1
print("marks more_than_50:"+str(more_than_50))
print("marks_less_than_50:"+str(less_than_50))
        
                                                                          