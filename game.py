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
    


def playRound(player, cpu):
    marks = ['   ','   ','   ','   ','   ','   ','   ','   ','   ']
    gr.grid(marks)
    turns = 0
    while turns < 9:
        playerTurn(player, marks)
        turns+=1
        print('turns ',turns)
        print()
        if(turns == 9):
            gr.grid(marks)
            break
        cpuTurn(cpu, marks)
        turns+=1
        print('turns ',turns)
        gr.grid(marks)
        

def playGame(player, cpu):
    yesNo = True
    r = 1
    while yesNo:
        print('Lets start round ', r, '!')
        print()
        playRound(player, cpu)
        yesNo = u.validYN('Do you want to play another round? ')
        r+=1