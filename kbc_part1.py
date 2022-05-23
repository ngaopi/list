# question_list=["what is the capital of India"]
# option_list=["Bhopal","Chandigarh","Chennai","Delhi"]
# solution_list=[4]
# i=0
# while i<len(question_list):
#     print("Q.",question_list[i])
#     j=0
#     while j<len(option_list):
#         print(j+1,option_list[j])
#         j=j+1
#     user=int(input("enter any number:"))
#     if user==solution_list[i]:
#         print("congrats you guessed the correct answer")
#     else:
#         print("sorry!you guessed the wrong answer")
#     i=i+1

question_list=["how many continents are there?","what is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
option_list=[["four","nine","eight","seven"],["Chandigarh","Bhopal","Delhi","Chennai"],["Software engineering","Tourism","Agriculture","Counseling"]]
solution_list=[4,3,1]
i=0
while i<len(question_list):
    print("Q.",i+1,question_list[i])
    j=0
    while j<len(option_list[i]):
        print(j+1,option_list[i][j])
        j=j+1
    user=int(input("enter any number:"))
    if user==solution_list[i]:
        print("congrats")
    else:
        print("sorry")
        break
    i=i+1
    
    