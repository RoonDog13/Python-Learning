from random import randint
game_state = True
user_score = 0
computer_score = 0
user_name = input("Type in your name: ")
number_games_string = input("How many games would you like to play")
number_games = int(number_games_string)
print("Ok the first one to get " + str(number_games) + " round wins, wins the game")

while game_state:
    user_choice = input("Choose 'ROCK', 'PAPER', 'SCISSORS' or 'Quit': ").lower()
    computer_choice_number = randint(1, 3)
    computer_choice = ''
    if computer_choice_number == 1:
        computer_choice = 'rock'
    elif computer_choice_number == 2:
        computer_choice = 'paper'
    elif computer_choice_number == 3:
        computer_choice = 'scissors'
    if user_choice == 'quit':
        game_state = False
##############
    elif user_choice == computer_choice:
        print("Its a DRAW... " + user_name + " chooses " +  user_choice + " and the computer also chooses " + computer_choice)
        print("The Current score is " + str(user_score) + ": for " + user_name + " and " + str(computer_score) + " for the computer")

    elif user_choice == 'rock' or computer_choice == 'rock':
        if user_choice == 'scissors':
            computer_score += 1
        else:
            user_score += 1
        print("The computer has chosen " + computer_choice + " and " + user_name + " has chosen " + user_choice)
        #print("User has won and has a score of " + str(user_score))
        
    elif user_choice == 'paper' and computer_choice == 'rock':
        user_score += 1
        print("The computer has chosen " + computer_choice + " and " + user_name + " has chosen " + user_choice)
        print("User has won and has a score of " + str(user_score))

    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("The computer has chosen " + computer_choice + " and " + user_name + " has chosen " + user_choice)
        user_score += 1
        print("User has won and has a score of " + str(user_score))

###############
    if computer_score == number_games:
        game_state = False
        print("The Current score is " + str(user_score) + ": for " +user_name +  "and " + str(computer_score) + " for the computer")
        print("The computer has won the game")
    elif user_score == number_games:
        gamee_state = False
        print("The Current score is " + str(user_score) + ": for "+ user_name + " and " + str(computer_score) + " for the computer")
        print(user_name + " has won the game")
        
