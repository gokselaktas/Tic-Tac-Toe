import random
import time

win1 = False
win2 = False
tie = False

board = [[" " for i in range(3)] for i in range(3)]# 3x3 her elemani "' '" olan matris

class colors:
    header = '\033[95m'
    cblue = '\33[34m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    fail = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    underline = '\033[4m'

def playerselect():
    global firstplayer
    firstplayer = random.randint(1, 2)
    if firstplayer == 1:
     p1 = True
     print("Player 1 Baslayacak...")
    else:
     p1 = False
     print("Player 2 Baslayacak...")
    return p1

def gameMenu():
    print(colors.header+"*************************************\n"\
          "*************************************\n"\
          "*************************************\n"\
          "*************"+colors.BOLD+"TIC-TAC-TOE"+colors.header+"*************\n"\
          "*************************************\n"\
          "*************************************\n"\
          "*************************************\n"+colors.yellow+\
          "1: for single player\n"\
          "2: for two player\n"\
          "3: for quit\n"+colors.ENDC)

    menu = int(input())
    if menu == 1:
        vsPC= True

    elif menu == 2:
        vsPC= False

    elif menu == 3:
        exit("Cikis yapiliyor...\n"\
             "Oyun kapatildi.")

    else:
        print("Gecersiz giris araligi...")
        gameMenu()

    print("ilk kimin baslayacagini belirlemek icin enter a basin...")
    first = input()
    time.sleep(0.2)
    return vsPC






def hamleAl(p1, vsPC):
    if not p1 and vsPC:
        global satir, sutun
        satir = random.randint(0,2)
        sutun = random.randint(0,2)
        if(satir < 0 or satir > 2 or sutun <0 or sutun>2 or not(board[satir][sutun]==" ")):
            hamleAl(p1, vsPC)
        else:
            print("\nComputer\n ")
    else:
        (print("\nPlayer1:"))if p1 else(print("\nPlayer2:"))
        satir = int(input("\nHamle yapmak istediginiz satir: "))-1
        if satir < 0 or satir >2:
            print(colors.fail+"\n Gecersiz hamle! Satir sayisi [1,3]∈Z olmalidir. "+colors.ENDC)
            hamleAl(p1, vsPC)
        sutun = int(input("\nHamle yapmak istediginiz sutun: "))-1

        if sutun < 0 or sutun > 2:
            print(colors.fail+"\nGecersiz hamle! Sutun sayisi [1,3]∈Z olmalidir. "+colors.ENDC)

        if (not(board[satir][sutun]) == " "):
            print("\nGecersiz hamle. Zaten oynanmis hamleyi oynadiniz.")
            hamleAl(p1, vsPC)



def hamleYap(p1, vsPC):
    hamleAl(p1, vsPC)
    if(vsPC or not(p1)):
        time.sleep(0.2)
    if (p1):
        board[satir][sutun] = "X"
    else:
        board[satir][sutun] = "O"




def kazanan():
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2]):#satir kontrol
            if board[i][0] == "X":
                return 'Player'
            elif(board[i][0]=="O"):
                return "Computer"
        elif(board[0][i] == board[1][i] and board[1][i] == board[2][i]):#sutun kontrol
            if (board[0][i] == "X"):
                return  "Player"
            elif(board[0][i] == "O"):
                return "Computer"
        elif((board[0][0] == board[1][1] and board[1][1] == board[2][2] )or\
             (board[0][2] == board[1][1] and board[1][1] == board[2][0])):#capraz kontrol
            if board[1][1] == "X":
                return  "Player"
            elif board[1][1] == "O":
                return "Computer"
    tie = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                tie = False
    if tie == True:
        return "Berabere"
    else:
        return ""


def printboard():
    s = ""
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                s += ("["+colors.blue+" X "+colors.ENDC+"]")
            elif board[i][j] == "O":
                s += ("["+colors.yellow+" O "+colors.ENDC+"]")
            else:
                s += ("["+colors.ENDC+"   "+colors.ENDC+"]")
            #s += ("["+board[i][j]+"]") # renklendirmeden once
        s += "\n"
    return s

def resetboard():
    for i in range(3):
        for j in range(3):
            board[i][j]=" "

def playAgain():
    print(colors.yellow+"Press Enter to Play Again\n"
          "Press '1' to Quit\n"+colors.ENDC)
    last = input()
    if last == "1":
        print(colors.fail+"Cikis yapiliyor...\n"+colors.ENDC)
        time.sleep(0.5)
        exit("Oyun kapatildi.")
    else:
        play()


def play():
    resetboard()
    vsPC = gameMenu()
    winner = ""
    p1=playerselect()
    print(printboard())
    while winner == "":
        print("\n")
        hamleYap(p1, vsPC)
        winner = kazanan()
        print(printboard())
        p1 = not p1
    if winner == "Player":
        print(colors.BOLD+"\n***Tebrikler Kazandiniz (^.^)***\n\n"+colors.ENDC)
        playAgain()
    elif winner == "Computer":
        print(colors.BOLD+"\n Maalesef kaybettiniz"+colors.ENDC)
        playAgain()
    elif winner == "Berabere":
        print(colors.BOLD+"\nBeraberlik"+colors.ENDC)
        playAgain()

play()#xd
