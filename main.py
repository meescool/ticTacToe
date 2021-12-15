'''
This program is a small console tic tac toe game

Author: Marcela Estrada
Date: 12/9/2021
'''

import player as p
import cpu as c
import grid as gr
import game as ga
def rules():
    print('These are rules of the game')
    print('---------------------------')
    print('Each player has a chance to place a symbol on '
            + 'the board that is printed out below:\n\n'
            + '   |   |   \n'
            + '===========\n'
            + '   |   |   \n'
            + '===========\n'
            + '   |   |   \n')
    print('In order to place a piece the player has the option\n'
            + 'has to enter a number from 1 to 9 which will place \n'
            + 'the piece in the following spots on the board:\n\n'
            + ' 1 | 2 | 3 \n'
            + '===========\n'
            + ' 4 | 5 | 6 \n'
            + '===========\n'
            + ' 7 | 8 | 9 \n')
    print('The player and the cpu will take turns until one of \n'
            + 'has three of their symbols in a row, column or \n'
            + 'diagonal as seen below or similar matter:\n\n')
    
    print(    '   | * |         |   | *       | * |   \n'
            + '===========   ===========   ===========\n'
            + '   | * |         | * |         | * |   \n'
            + '===========   ===========   ===========\n'
            + '   | * |       * |   |         | * |   \n')
    
def main():
    print("Welcome to Tic Tac Toe!!")
    rules()
    player = p.setPlayer()
    cpu = c.setCPU(player)
    ga.playGame(player, cpu)



if __name__ == "__main__":
    main()