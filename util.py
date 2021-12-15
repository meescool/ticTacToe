import time

characters = [' o ',' x ',' <3',' $ ','zzz']


def validNum(prompt, min, max):
    '''
    This function returns the number if it's a valid number
    '''
    userIn = input(prompt)
    while True:
        try:
            num = int(userIn)
            if(num >= min and num <= max):
                num = num - min
                return num

        except ValueError:
              print('Invalid input!', 'Please enter a number between ', min , ' and ', max, ' ')
              userIn = input()


def validYN (prompt):
    while True:
        userIn = input(prompt)
        if(userIn == 'y' or userIn == 'yes'):
            return True
        if(userIn == 'n' or userIn == 'no'):
            return False
        else:
            print('Invalid input!', end =" " )
            


        


def showCharacters():
    
    i = 1

    for c in characters:
        print( i, ') ', c)
        i += 1

def waitTime(t):
    for i in range(t):
        time.sleep(1)
        print('processing ...')
      
