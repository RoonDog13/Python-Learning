from random import randint
game_state = True
number_of_guesses = 0
computer_number = randint(0,20)
while game_state and number_of_guesses < 6:
    user_guess = (int (input("Guess a number between 0 and 20: ")))
    number_of_guesses +=1
    if user_guess == computer_number:
        print("You got the number!")
        game_state = False
    elif user_guess < computer_number:
        print("You guessesed too low")
    elif user_guess > computer_number:
        print("You guessed too high")
