mport random
print("welcome to RPS GAME")

user_score = 0
computer_score = 0
tie = 0
name= input("Enter your name here:")
print("""win's rule:
1. Paper vs Rock --> Paper
2. Rock vs Scissor --> Rock
3. Scissor vs Paper --> Scissor""") 

print()

print("""choices are:
1. Rock
2. Paper
3. Scissor""")

print()
while True:
 user_choice = int(input("Enter your choice from 1-3: "))

 print()

 while user_choice > 3 or user_choice < 1:
      user_choice = int(input("enter valid input"))

 if user_choice == 1:
    user_choice = "Rock"
 elif user_choice == 2:
     user_choice = "Paper"
 elif user_choice == 3:
     user_choice == "Scissor"
 else:
     print("its a invalid ")

 print(name,"'s choice is",user_choice)
 print("Now it is computer turn")

 computer_choice = random.randint(1,3)
 
 if computer_choice == 1:
   computer_choice = "Rock"
 elif computer_choice == 2:
     computer_choice = "Paper"
 else:
     computer_choice == "Scissor"

 print("The computer's choice is", computer_choice)

 if((user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Rock" and computer_choice == "Paper")):
    print("Paper wins")
    result = "Paper"
 elif((user_choice == "Scissor" and computer_choice == "Rock") or (user_choice == "Rock" and computer_choice == "Scissor")):
      print("Rock wins")
      result = "Rock"
 elif(user_choice == computer_choice):
      print("it's tie")
      result="tie"
 
 
 else:
      print("Scissor wins")
      result="Scissor"


 if result == "tie":
    tie += 1
 elif result == user_choice:
      user_score += 1
 else:
      computer_score += 1

 print("Scores are")
 print(name,"'s have "+str(user_score)+" score")
 print("computer's " +str(computer_score)+" score")
 print("tie have "+str(tie)+" score")

 repeat= input("\n play again? (yes/no): ")
 if repeat.lower() != "yes":
       break
       print("game over")
       print("-------thanks for playing--------")

     
