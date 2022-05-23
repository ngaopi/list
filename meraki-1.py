# student_list=['helen','susan','gabriel']
# length=len(student_list)
# index=0 
# while index < length:
#     print(student_list[index])
#     index=index+1

# calculate the total marks of a student from the student's marks list

student_marks=[23,45,89,90,56,80]
lenght=len(student_marks)
index=0
total_marks=0
while index < len(student_marks):
    total_marks=student_marks[index]+total_marks
    index=index+1
print("total_marks:"+str(total_marks))



    