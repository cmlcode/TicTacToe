import random
import os

global board1
global board2
global board3
global player

def clear():
    os.system("cls")

def start():
        global turn
        global board1
        global board2
        global board3
        turn=0
        board1=["1","2","3"]
        board2=["4","5","6"]
        board3=["7","8","9"]

        try:
            playerCount=int((input("Play with 1 player or 2?\n")))
        except:
            print("Please enter the digit 1 or 2")
            start()
        clear()
        if playerCount==1:
            playOrder1()
        elif playerCount==2:
            playOrder2()
        else:
            start()
def getInput(choice):
    if choice==0:
        try:
            pos=int(input("Where would you like to play?\n"))
        except:
            print("Please enter a digit 1-9")
            getInput(0)
        if not(pos>0 and pos<10):
            print("Please enter a digit 1-9")
            getInput(0)
        return pos
def printBoard():
    print(board1)
    print(board2)
    print(board3)
def playOrder1():
    player=random.randint(0,1)
    if player==0:
        player0()
    player1()
def playOrder2():
     player=random.randint(2,3)
     if player==2:
        player2()
     player3()
def player0():
    global turn
    pos=-1
    turn+=1
    print("X'S TURN")
    printBoard()
    pos=getInput(0)

    if pos<=3:
        pos-=1
        if board1[pos]!="O" and board1[pos]!="X":
            board1[pos]="X"
        else:
            print("Spot already in use")
            player0()
    elif pos<=6:
        pos-=4
        if board2[pos]!="O" and board2[pos]!="X":
            board2[pos]="X"
        else:
            print("Spot already in use")
            player0()
    else:
        pos-=7
        if board3[pos]!="O" and board3[pos]!="X":
            board3[pos]="X"
        else:
            print("Spot already in use")
            player0()
    checkBoard("X")
    clear()
    player1()
def player1():
    global turn
    if turn%2==0:
        first()
    else:
        second()
    turn+=1
    checkBoard("O")
    player0()
def first():
    if findWin():
        print("findWin")
        checkBoard("O")
        return None
    if block():
        return None
    if turn==0:
        board3[0]="O"
    elif turn==2:
        if board2[2]=="6":
            if board3[2]=="9":
                board3[2]="O"
            else:
                board1[0]="O"
        else:
            if futWin():
                return None
            rand()
    elif turn==4:
        if board3[2]=="O":
            if board1[0]=="1":
                board1[0]="O"
            else:
                board1[2]="O"
        elif board1[0]=="1":
            if board1[2]=="3":
                board1[2]="O"
        else:
            if futWin():
                return None
            rand()
    else:
        if futWin():
            return None
        rand()
    checkBoard("O")
def second():
    if findWin():
        print("findWin")
        checkBoard("O")
        return None
    if block():
        return None
    if futWin():
        return None
    if board1[1]=="5":
        board1[1]=="O"
        return None
    rand()
def futWin():
    if board1[0]=="O" and board1[1]=="2" and board1[2]=="3":
        board1[2]="O"
        return True
    elif board1[0]=="1" and board1[1]=="2" and board1[2]=="O":
        board1[0]="O"
        return True
    elif board1[0]=="1" and board1[1]=="O" and board1[2]=="3":
        board1[0]="O"
        return True
    elif board2[0]=="O" and board2[1]=="5" and board2[2]=="6":
        board2[2]="O"
        return True
    elif board2[0]=="4" and board2[1]=="5" and board2[2]=="O":
        board2[0]="O"
        return True
    elif board2[0]=="4" and board2[1]=="O" and board2[2]=="6":
        board2[0]="O"
        return True
    elif board3[0]=="O" and board3[1]=="8" and board3[2]=="9":
        board3[2]="O"
        return True
    elif board3[0]=="7" and board3[1]=="8" and board3[2]=="O":
        board3[0]="O"
        return True
    elif board3[0]=="7" and board3[1]=="O" and board3[2]=="9":
        board3[0]="O"
        return True
    elif board1[0]=="O" and board2[0]=="4" and board3[0]=="7":
        board2[0]="O"
        return True
    elif board1[0]=="1" and board2[0]=="4" and board3[0]=="O":
        board1[0]="O"
        return True
    elif board1[0]=="1" and board2[0]=="O" and board3[0]=="7":
        board1[0]="O"
        return True
    elif board1[1]=="O" and board2[1]=="5" and board3[1]=="8":
        board2[1]="O"
        return True
    elif board1[1]=="2" and board2[1]=="5" and board3[1]=="O":
        board1[1]="O"
        return True
    elif board1[1]=="2" and board2[1]=="O" and board3[1]=="8":
        board1[1]="O"
        return True
    elif board1[2]=="O" and board2[2]=="6" and board3[2]=="9":
        board2[2]="O"
        return True
    elif board1[2]=="3" and board2[2]=="6" and board3[2]=="O":
        board1[2]="O"
        return True
    elif board1[2]=="3" and board2[2]=="O" and board3[2]=="9":
        board1[2]="O"
        return True
    elif board1[0]=="O" and board2[1]=="5" and board3[2]=="8":
        board3[2]="O"
        return True
    elif board1[0]=="1" and board2[1]=="5" and board3[2]=="O":
        board1[0]="O"
        return True
    elif board1[0]=="1" and board2[1]=="O" and board3[2]=="8":
        board1[0]="O"
        return True
    elif board3[0]=="7" and board2[1]=="5" and board1[2]=="3":
        board1[2]="O"
        return True
    elif board3[0]=="7" and board2[1]=="5" and board1[2]=="3":
        board3[0]="O"
        return True
    elif board3[0]=="7" and board2[1]=="O" and board1[2]=="3":
        board3[0]="O"
        return True
    return False
def rand():
    open=[]
    count=0
    for spot in board1:
        if spot!="X" and spot!="O":
            open.append(count)
        count+=1
    for spot in board2:
        if spot!="X" and spot!="O":
            open.append(count)
        count+=1
    for spot in board3:
        if spot!="X" and spot!="O":
            open.append(count)
        count+=1
    choice=open[random.randint(0,len(open)-1)]
    if choice<3:
        board1[choice]="O"
    elif choice<6:
        board2[choice-3]="O"
    elif choice<9:
        board3[choice-6]="O"
def block():
    if board1[0]=="X":
        if board3[2]=="X":
            if board2[1]=="5":
                board2[1]="O"
                return True
            elif board1[2]=="X":
                if board1[1]=="2":
                    board1[1]="O"
                    return True;
                elif board2[2]=="6":
                    board2[2]="O"
                    return True;
                elif board3[0]=="X":
                    if board2[0]=="4":
                        board2[0]="O"
                        return True;
                    elif board3[1]=="8":
                        board3[1]="O"
                        return True;
            elif board3[0]=="X":
                if board2[0]=="4":
                    board2[0]="O"
                    return True;
                elif board3[1]=="8":
                    board3[1]="O"
                    return True;
        elif board1[2]=="X":
            if board1[1]=="2":
                board1[1]="O"
                return True;
            elif board3[0]=="X":
                if board2[0]=="4":
                    board2[0]="O"
                    return True;
                elif board2[1]=="5":
                    board2[0]="O"
                    return True;
            elif board2[0]=="X" and board2[1]=="X" and board2[2]=="6":
                board2[2]="O"
                return True;
            elif board2[0]=="X" and board2[1]=="5" and board2[2]=="X":
                board2[1]="O"
                return True;
            elif board2[0]=="4" and board2[1]=="X" and board2[2]=="X":
                board2[0]="O"
                return True;
        elif board1[1]=="X" and board1[2]=="3":
            board1[2]="O"
            return True;
        elif board1[1]=="2" and board1[2]=="X":
            board1[1]="O"
            return True;
        elif board2[0]=="4" and board3[0]=="X":
            board2[0]="O"
            return True;
        elif board2[0]=="X" and board3[0]=="7":
            board3[0]="O"
            return True;
    elif board3[2]=="X":
        if board1[2]=="X":
            if board2[2]=="6":
                board2[2]="O"
                return True;
            elif board2[1]=="X":
                if board1[1]=="X" and board3[1]=="8":
                    board3[1]="O"
                    return True
                if board1[1]=="2" and board3[1]=="X":
                    board1[1]="O"
                    return True
                elif board3[0]=="7":
                    board3[0]="O"
                    return True
            elif board3[0]=="7" and board3[1]=="X":
                board3[0]="O"
                return True
            elif board3[0]=="X" and board3[1]=="8":
                board3[1]="X"
        elif board3[0]=="X" and board3[1]=="8":
            board3[1]="O"
            return True
        elif board3[0]=="7" and board3[1]=="X":
            board3[0]="O"
            return True
        elif board2[0]=="X" and board2[1]=="X" and board2[2]=="6":
                board2[2]="O"
                return True
        elif board2[0]=="O" and board2[1]=="5" and board2[2]=="O":
                board2[1]="O"
                return True
        elif board2[0]=="4" and board2[1]=="X" and board2[2]=="X":
                board2[0]="O"
                return True
        return False
    elif board2[1]=="X":
        if board1[2]=="X":
            if board3[0]=="7":
                board3[0]="O"
                return True;
        elif board2[0]=="X":
            if board2[2]=="6":
                board2[2]="O"
                return True;
        elif board2[2]=="X":
            if board2[0]=="4":
                board2[0]="O"
                return True
        elif board1[1]=="2" and board3[1]=="X":
            board1[1]="O"
            return True;
        elif board1[1]=="X" and board3[1]=="8":
            board3[1]="O"
            return True;
def findWin():
    if board1[0]=="O":
        if board3[2]=="O":
            if board2[1]=="7":
                board2[1]="O"
            elif board1[2]=="O":
                if board1[1]=="2":
                    board1[1]="O"
                elif board2[2]=="6":
                    board2[2]="O"
                elif board3[0]=="O":
                    if board2[0]=="4":
                        board2[0]="O"
                    elif board3[1]=="8":
                        board3[1]="O"
            elif board3[0]=="O":
                if board2[0]=="4":
                    board2[0]="O"
                elif board3[1]=="8":
                    board3[1]="O"
        elif board1[2]=="O":
            if board1[1]=="2":
                board1[1]="O"
            elif board3[0]=="O":
                if board2[0]=="1":
                    board2[0]="O"
                elif board2[1]=="5":
                    board2[0]="O"
            elif board2[0]=="O" and board2[1]=="O" and board2[2]=="6":
                board2[2]="O"
            elif board2[0]=="O" and board2[1]=="5" and board2[2]=="O":
                board2[1]="O"
            elif board2[0]=="4" and board2[1]=="O" and board2[2]=="O":
                board2[0]="O"
        elif board1[1]=="O" and board1[2]=="3":
            board1[2]="O"
        elif board1[1]=="2" and board1[2]=="O":
            board1[1]="O"
        elif board2[0]=="4" and board3[0]=="O":
            board2[0]="O"
        elif board2[0]=="O" and board3[0]=="7":
            board3[0]="O"
    elif board3[2]=="O":
        if board1[2]=="O":
            if board2[2]=="8":
                board2[2]="O"
                return True
            elif board2[1]=="O":
                if board1[1]=="O" and board3[1]=="8":
                    board3[1]="O"
                    return True
                if board1[1]=="2" and board3[1]=="O":
                    board1[1]="O"
                    return True
                elif board3[0]=="7":
                    board3[0]="O"
                    return True
            elif board3[0]=="7" and board3[1]=="O":
                board3[0]="O"
                return True
            elif board3[0]=="O" and board3[1]=="8":
                board3[1]="X"
                return True
        elif board3[0]=="O" and board3[1]=="8":
            board3[1]="O"
            return True
        elif board3[0]=="7" and board3[1]=="O":
            board3[0]="O"
            return True;
        elif board2[0]=="O" and board2[1]=="O" and board2[2]=="6":
                board2[2]="O"
                return True;
        elif board2[0]=="O" and board2[1]=="5" and board2[2]=="O":
                board2[1]="O"
                return True;
        elif board2[0]=="4" and board2[1]=="O" and board2[2]=="O":
                board2[0]="O"
                return True;
    elif board2[1]=="O":
        if board1[2]=="O":
            if board3[0]=="7":
                borad3[0]="O"
                return True;
        elif board2[0]=="O":
            if board2[2]=="6":
                board2[2]="O"
                return True;
    return False;
def player2():
    global turn
    turn+=1
    print("X'S TURN")
    printBoard()
    pos=getInput(0)
    if pos<=3:
        pos-=1
        if board1[pos]!="O" and board1[pos]!="X":
            board1[pos]="X"
        else:
            print("Spot already in use")
            player2()
    elif pos<=6:
        pos-=4
        if board2[pos]!="O" and board2[pos]!="X":
            board2[pos]="X"
        else:
            print("Spot already in use")
            player2()
    else:
        pos-=7
        if board3[pos]!="O" and board3[pos]!="X":
            board3[pos]="X"
        else:
            print("Spot already in use")
            player2()
    checkBoard("X")
    clear()
    player3()
def player3():
    global turn
    turn+=1
    print("O'S TURN")
    printBoard()
    pos=getInput(0)
    if pos<=3:
        pos-=1
        if board1[pos]!="O" and board1[pos]!="X":
            board1[pos]="O"
        else:
            print("Spot already in use")
            player3()
    elif pos<=6:
        pos-=4
        if board2[pos]!="O" and board2[pos]!="X":
            board2[pos]="O"
        else:
            print("Spot already in use")
            player3()
    else:
        pos-=7
        if board3[pos]!="O" and board3[pos]!="X":
            board3[pos]="O"
        else:
            print("Spot already in use")
            player3()
    checkBoard("O")
    clear()
    player2()
def checkBoard(player):
    if board1[0]==player:
        if board3[2]==player:
            if board2[1]==player:
                gameOver(player)
            elif board1[2]==player:
                if board1[1]==player or board2[2]==player:
                    gameOver(player)
                elif board3[0]==player:
                    if board2[0]==player or board3[1]==player:
                        gameOver(player)
            elif board3[0]==player:
                if board2[0]==player or board3[1]==player:
                    gameOver(player)
        elif board1[2]==player:
            if board1[1]==player:
                gameOver(player)
            elif board3[0]==player:
                if board2[0]==player or board2[1]==player:
                    gameOver(player)
            elif board2[0]==player and board2[1]==player and board2[2]==player:
                gameOver(player)
        elif board1[1]==player and board1[2]==player:
            gameOver(player)
        elif board2[0]==player and board3[0]==player:
            gameOver(player)

    elif board3[2]==player:
        if board1[2]==player:
            if board2[2]==player:
                gameOver(player)
            elif board2[1]==player:
                if (board1[1]==player and board3[1]==player) or board3[0]==player:
                    gameOver(player)
            elif board3[0]==player and board3[1]==player:
                gameOver(player)
        elif board3[0]==player and board3[1]==player:
            gameOver(player)
        elif board2[0]==player and board2[1]==player and board2[2]==player:
            gameOver(player)
    elif board2[1]==player:
        if board1[2]==player:
            if board3[0]==player:
                gameOver(player)
        elif board2[0]==player:
            if board2[2]==player:
                gameOver(player)
        elif board1[1]==player and board3[1]==player:
            gameOver(player)
    if turn==9:
        tie()
def gameOver(player):
    clear()
    print('\033[1m' + "Player" ,player,"won" +'\033[1m\n')
    printBoard()
    end()
def tie():
    clear()
    print('\033[1m' + "There was a tie" +'\033[1m\n')
    printBoard()
    end()
def end():
    again=input("Would you like to play again (Y/N)\n")
    if again=="Y":
        start()
    else:
        exit(0)

start()

