import random
def Rock_Paper_Scissors_Game():
    # Creating a list containing all the main items of the game.
    choices = ["rock", "paper", "scissors"]

    player_score = 0 # Storing Player's score.
    computer_score = 0 # Storing computer's score.
    draws = 0 # Storing Draws data.

    # Intro
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("This Game have only one rule: WRITE YOUR ANSWER IN LOWERCASE LETTER!")
    print(f"Score -> You: {player_score} | Computer: {computer_score} | Draws: {draws}\n")

    # Creating a infinite loop till the user chooses quit.
    while True: 
        computer_choice = random.choice(choices) # Using random.choices to randomly choose the string from the list.
            
        player = input(f"Enter your choice (rock/paper/scissors) or quit: ") # Taking User's choice

        player_choice = player.lower() # The user choice could be in any type. So we use .lower() to lowercase the input entered by the user

        if(player not in choices and player_choice != "quit"): # Telling User if his input is not correct
            print("\nError: Please enter correct spelling or enter lowercase letter answer.\n")
            continue

        # If user choose quit
        if(player_choice == "quit"):
            print(f"\nFinal Score -> You: {player_score} | Computer: {computer_score} | Draws: {draws}")
            print("Thanks for playing!")
            break

        print(f"Computer choose: {computer_choice}") # Telling user that what computer has choose.

        # Conditions
        if (player_choice == computer_choice):
            print("Its a tie!\n")
            draws += 1
        elif (player_choice == "rock" and computer_choice == "scissors"):
            print("You win this round!\n")
            player_score += 1
        elif (player_choice == "paper" and computer_choice == "rock"):
            print("You win this round!\n")
            player_score += 1
        elif (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!\n")
            player_score += 1
        else:
            print("You lose the round! Try again!\n")
            computer_score += 1

        print(f"Score -> You: {player_score} | Computer: {computer_score} | Draws: {draws}") # Printing score after every round.


Rock_Paper_Scissors_Game()
