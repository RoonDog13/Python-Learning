import random
user_score = 0
computer_score = 0
objects = ['Rock', 'Paper', 'Scissors']

Win_Condition = {'Rock': 'Scissors',
                 'Paper': 'Rock',
                 'Scissors': ['Paper','bazooka'],
                 }

Play_Again = True
while Play_Again is True:
    human_input = input('Pick Rock, Paper, or Scissors: ')
    print('Human picked: ', human_input)
    computer_input = objects[random.randint(0,2)]
    print('Computer picked: ', computer_input)
    if human_input == computer_input:
        print('Tie')
        Play_Again = input('Would you like to Play Again? (True/False): ')
    elif Win_Condition[human_input] == computer_input:
        print('Humans beat the Machines.')
        user_score += 1
        print("The score is " + user_score + " for the user and " + computer_score + " for the computer")
        Play_Again = input('Would you like to Play Again? (True/False): ')
        
    else:
        print('AI Takeover.')
        computer_score +=1
        print("The score is " + user_score + " for the user and " + computer_score + " for the computer")
        Play_Again = input('Would you like to Play Again? (True/False): ')
