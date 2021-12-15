import util as u
import grid as gr
def playerTurn(player, marks):
    print('Your turn! (Input a number between 1 and 9)')
    u.validNum

def cpuTurn(player):
    print('CPU turn!')
    u.waitTime(2)


def playRound(player, cpu):
    marks = ['   ','   ','   ','   ','   ','   ','   ','   ','   ']
    gr.grid(marks)
    while True:
        plays = playerTurn(player, marks)
        plays = cpuTurn(cpu)
        gr.grid(marks)
        break
        

def playGame(player, cpu):
    yesNo = True
    r = 1
    while yesNo:
        print(player)
        print('Lets start round ', r, '!')
        playRound(player, cpu)
        print(cpu)
        yesNo = u.validYN('Do you want to play another round? ')
        r+=1