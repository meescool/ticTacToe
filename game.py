import random
import util as u
import grid as gr

def setMark(playerName, marks, type):
    while True:
        if type == 'p':
            tempMark= u.validNum('(Input a number between 1 and 9) ', 1, 9)
        else:
            tempMark= random.randrange(0,8)
        if(marks[tempMark] == '   '):
            marks[tempMark] = playerName['char']
            break

def playerTurn(player, marks):
    print('Your turn!')
    setMark(player, marks, 'p')
 

def cpuTurn(cpu, marks):
    print('CPU turn!')
    setMark(cpu, marks, 'c' )
    u.waitTime(2)

def printWinner(mark, player, cpu, ):
    
    if(mark == player['char']):
        player['wins'] += 1
        print("Hurray! You won this round!")
    else:
        print("CPU won. Better luck next time!")
    

        
def checkWinner(player, cpu, marks):
    if(marks[0] == marks[1] and marks[0] == marks[2] and marks[0] != '   '):
        printWinner(marks[0], player, cpu)
    elif(marks[0] == marks[4] and marks[0] == marks[8] and marks[0] != '   '):
        printWinner(marks[0], player, cpu)
    elif(marks[0] == marks[3] and marks[0] == marks[6] and marks[0] != '   '):
        printWinner(marks[0], player, cpu)
    
    elif(marks[1] == marks[4] and marks[1] == marks[7] and marks[1] != '   '):
        printWinner(marks[1], player, cpu)

    elif(marks[2] == marks[4] and marks[2] == marks[6] and marks[2] != '   '):
        printWinner(marks[2], player, cpu)
    elif(marks[2] == marks[5] and marks[2] == marks[8] and marks[2] != '   '):
        printWinner(marks[2], player, cpu)

    elif(marks[3] == marks[4] and marks[3] == marks[5] and marks[3] != '   '):
        printWinner(marks[3], player, cpu)

    elif(marks[6] == marks[7] and marks[6] == marks[8] and marks[6] != '   '):
        printWinner(marks[6], player, cpu)
    else:
        return False

    return True
        

def playRound(player, cpu):
    marks = ['   ','   ','   ','   ','   ','   ','   ','   ','   ']
    gr.grid(marks)
    turns = 0
    while turns < 9:
        playerTurn(player, marks)
        turns+=1
        gr.grid(marks)
        print()
        if(checkWinner(player, cpu, marks) == True):
            print(marks)
            break
        if(turns == 9):
            print("Tie! No one won.")
            break
        cpuTurn(cpu, marks)
        gr.grid(marks)
        if(checkWinner(player, cpu, marks) == True):
            print(marks)
            break
        turns+=1
        print('turns ',turns)
        
        

def playGame(player, cpu):
    yesNo = True
    r = 0
    while yesNo:
        r+=1
        print('Lets start round ', r, '!')
        print()
        playRound(player, cpu)
        yesNo = u.validYN('Do you want to play another round? ')
        
    print("You won a total of ", player['wins'], " out of ", r)
    print("Thanks for playing! Good bye.")