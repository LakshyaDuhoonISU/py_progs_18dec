#rock paper scissors game
import random
print("Welcome to Rock Paper Scissors!")
def playerchoice():
    global a
    a=["ROCK","PAPER","SCISSORS"]
    global b
    b=int(input("Enter your choice:\n1.Rock\n2.Paper\n3.Scissors\n"))
    while b<1 or b>3:
        print("Invalid choice")
        b=int(input("Enter your choice:\n1.Rock\n2.Paper\n3.Scissors\n"))
    print("Player:",a[b-1])
def compchoice():
    global d
    d=random.randint(0,2)
    print("Computer:",a[d])
def winner():
    if a[b-1]==a[d]:
        print("TIE")
    elif a[b-1]=="ROCK" and a[d]=="SCISSORS":
        print("Winner: User")
    elif a[b-1]=="SCISSORS" and a[d]=="PAPER":
        print("Winner: User")
    elif a[b-1]=="PAPER" and a[d]=="ROCK":
        print("Winner: User")
    else:
        print("Winner: Computer")
while True:
    playerchoice()
    compchoice()
    winner()
    e=input("Want to play again?(y/n): ")
    if e.lower()=="n":
        break