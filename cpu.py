import time
import util as u
import random

def cpuChoose(type, playerChar):
    random.seed()
    if type == 'c':
        while True:
            op = random.choice(u.characters)
            print( op)
            if op != playerChar:
                return op
        
def setCPU(player):
    print('The computer will now choose its character')
    print()
    u.waitTime(3)
    print()
    op = cpuChoose('c', player.get('char'))
    cpu = {
        'char': op,
        'wins': 0
    }

    print('The computer chose: ', cpu)
    return cpu
