import util as u
def playGame(player, cpu):
    yesNo = True
    while yesNo:
        print(player)
        print(cpu)
        yesNo = u.validYN('Do you want to play another round? ')