#tictactoe game
a=[["","",""],["","",""],["","",""]]
def clearboard():
    for i in range(3):
        for j in range(3):
            a[i][j] =" "
def printboard():
    print(a[0][0],"|",a[0][1],"|",a[0][2])
    print("--|---|--")
    print(a[1][0],"|",a[1][1],"|",a[1][2])
    print("--|---|--")
    print(a[2][0],"|",a[2][1],"|",a[2][2])
def checkmove(d,e):
    if d<1 or d>len(a)+1:
        print("Invalid move")
        return 1
    if e<1 or e>len(a)+1:
        print("Invalid move")
        return 1
    if a[d-1][e-1]!=" ":
        print("Invalid move")
        return 0
def checkwin():
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] == "X":
            print("Player 1 wins")
            return 1
        elif a[i][0] == a[i][1] == a[i][2] == "O":
            print("Player 2 wins")
            return 1
        if a[0][i] == a[1][i] == a[2][i] == "X":
            print("Player 1 wins")
            return 1
        elif a[0][i] == a[1][i] == a[2][i] == "O":
            print("Player 2 wins")
            return 1
    if a[0][0] == a[1][1] == a[2][2] == "X":
        print("Player 1 wins")
        return 1
    elif a[0][0] == a[1][1] == a[2][2] == "O":
        print("Player 2 wins")
        return 1

    if a[0][2] == a[1][1] == a[2][0] == "X":
        print("Player 1 wins")
        return 1
    elif a[0][2] == a[1][1] == a[2][0] == "O":
        print("Player 2 wins")
        return 1
    return 0
def checkboard():
    for i in range(3):
        for j in range(3):
            if a[i][j]==" ":
                return 0
    print("Board full!")
    return 1
def game():
    printboard()
    print("Player 1- X\nPlayer 2-O")
    currentPlayer=1
    while True:
        e=checkwin()
        if e==1:
            break
        f=checkboard()
        if f==1:
            break
        print("Player",currentPlayer)
        g=int(input("Enter row number(1-3): "))
        h=int(input("Enter column number(1-3): "))
        d=checkmove(g,h)
        if d==1:
            break
        elif d==0:
            game()
        if currentPlayer==1:
            a[g-1][h-1]="X"
            printboard()
        else:
            a[g-1][h-1]="O"
            printboard()
        currentPlayer=1 if currentPlayer==2 else 2
clearboard()
print("Welcome to Tic-Tac-Toe!")
game()