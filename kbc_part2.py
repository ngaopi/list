question_list=[["what is the capital of India"],["How many continents are there"],["which course is being taught in Navgurukul"]]
option_list=[["Chandigarh","Bhopal","Delhi","Chennai"],["Four","Nine","Eight","Seven"],["Software-Engineering","Tourism","Agriculture","Counseling"]]
life_line=[["Bhopal","Delhi"],["Seven","Eight"],["Agriculture","Software-Engineering","Agriculture"]]
life_solution=[2,1,2]
solution_list=[3,4,1]
i=0
count=0
while i<len(question_list):
    print("Q",i+1,question_list[i])
    j=0
    while j<len(option_list[i]):
        print(j+1,option_list[i][j])
        j=j+1
    user=("1 without lifeline","2 with lifeline")
    choice=int(input("enter your choice 1 or 2."))
    if choice==1:
        user1=int(input("enter your answer."))
        if user1==solution_list[i]:
            print("WOW!"," CONGRATULATIONS","\n","go ahead")
        else:
            print("wrong answer!","\n","you cant move further","\n","restart the game")
            break
    elif choice==2:
        if count==0:
            k=0
            while k<len(life_line[i]):
                print(k+1,life_line[i][k])
                k=k+1
            count=count+1
            user2=int(input("enter your answer:"))
            if user2==life_solution[i]:
                print("WOW! congratulations","\n","you did it")
            else:
                print("wrong answer","\n","sorry...please restart")
                break 
        else:
            print("you have used your lifeline")
            user3=int(input("enter your answer: "))
            if user3==solution_list[i]:
                print("OK")
            else:
                print("bye bye")
                break
    else:
        print("we are so sorry for the inconvenience")
        break
    i=i+1
