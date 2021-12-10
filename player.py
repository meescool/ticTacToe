def showCharacters():
    characters = [' o ',' x ',' <3',' $ ','zzz']
    i = 1

    for c in characters:
        print( i, ') ', c)
        i += 1

def setPlayer():
    print('Lets choose your character!')
    print('You can choose from any of the characters\n'
        + 'seen below: ')
    showCharacters()
    
    op = input('which one do you want?')
