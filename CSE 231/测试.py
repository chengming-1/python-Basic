''' Use these strings when displaying messages to the user
         "Are you ready to play?"
         "Error: Invalid input."
         "Guess an integer between 1 and 100 (or Quit to stop game): "
         "Invalid input."
         "Your guess was correct!"
         "You win!"
         "You will be missed"
'''
from CSE201_random import randint
print("Guess the Number")

while True:
    print("Are you ready to play?")
    WantToPlayOrNot = input()    
    if WantToPlayOrNot.lower() == 'quit':
        print('you will be missed')
        break
    if WantToPlayOrNot.lower() =='yes':
        while True:
            random_num = randint(1, 100)
            print('Guess an integer between 1 and 100 (or Quit to stop game):')
            num_guessed = input()
            if num_guessed.lower() == 'quit':
                print('you will be missed')
                break
            if int(num_guessed) > 100:
                print('Invalid input.')
            if int(num_guessed) < 1:
                print('Invalid input.')
            if type(num_guessed) != int:
                print('Invalid input.')
            else:
                if 100 > int(num_guessed) > int(random_num):
                    print('Your guess was too high.')
                elif 1 < int(num_guessed) < int(random_num):
                    print('Your guess was too low.')
                elif int(num_guessed) == int(random_num):
                    print('You win!')
        break
    else:
        print("Error: Invalid input.")