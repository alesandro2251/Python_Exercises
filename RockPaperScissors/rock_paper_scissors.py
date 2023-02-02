import random

playerPick = int(input('Choose Rock (1), Paper (2) or Scissors (3) : '))

if playerPick == 1:
    print('You picked Rock !')
elif playerPick == 2:
    print('You picked Paper !')
elif playerPick == 3:
    print('You picked Scissors !')
else:
    print('Wrong choice ! Reset and try again !')

computerPick = random.randint(1, 3)

if computerPick == 1 and playerPick == 1:
    print('Rock vs Rock !')
    print('Draw !')
elif computerPick == 1 and playerPick == 2:
    print('Rock vs Paper! ')
    print('You Won ! ')
elif computerPick == 1 and playerPick == 3:
    print('Rock vs Scissors! ')
    print('Computer Won ! ')
elif computerPick == 2 and playerPick == 1:
    print('Paper vs Rock! ')
    print('Computer Won ! ')
elif computerPick == 2 and playerPick == 2:
    print('Paper vs Paper! ')
    print('Draw ! ')
elif computerPick == 2 and playerPick == 3:
    print('Paper vs Scissors! ')
    print('You Won ! ')
elif computerPick == 3 and playerPick == 1:
    print('Scissors vs Rock! ')
    print('You Won ! ')
elif computerPick == 3 and playerPick == 2:
    print('Scissors vs Paper! ')
    print('Computer Won ! ')
elif computerPick == 3 and playerPick == 3:
    print('Scissors vs Scissors! ')
    print('Draw! ')
