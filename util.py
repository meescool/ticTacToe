import time

characters = [' o ',' x ',' <3',' $ ','zzz']


def validNum(userIn, min, max):
    '''
    This function returns the number if it's a valid number
    '''

    while True:
        try:
            num = int(userIn)
            if(num >= min and num <= max):
                num = num - min
                return num

        except ValueError:
              print('Please enter a number between ', min , ' and ', max)
              userIn = input()

def showCharacters():
    
    i = 1

    for c in characters:
        print( i, ') ', c)
        i += 1

def waitTime(t):
    for i in range(t):
        time.sleep(1)
        print('processing ...')
      
