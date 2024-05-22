import random 

options = ('rock','paper','scissor')

print('Welcome to Rock-Paper-Scissor game !\n')

while True:
    computer = random.choice(options)
    player= input('Enter a choice(rock, paper, scissor): ')

    if player not in options:
        print('Invalid input. Try again')
        break
    else:
        print(f'\nYou picked: {player}')
        print(f'computer picked: {computer}')

        if player == computer:
            print('It is a draw\n')
        elif player == 'rock' and computer == 'scissor':
            print('You win !\n')
        elif player =='paper' and computer == 'rock':
            print('You win !\n')
        elif player == 'scissor' and computer== 'paper':
            print('You win !\n')
        else:
            print('You lost !\n')