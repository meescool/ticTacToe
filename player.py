import util as u


def setPlayer():
    player = {}
    print('Lets choose your character!')
    print('You can choose from any of the characters\n'
        + 'seen below: ')
    u.showCharacters()
    
    op = u.validNum(input('which one do you want? '), 1, 5)
    player = {
        'char': u.characters[op],
        'plays': [],
        'wins': 0,
    }

    print('You chose: ', player['char'])
    return player
