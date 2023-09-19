"""
This is the example basic game I want to build in every language I begin to learn.

It is the online game of Rock, Paper, Scissors.
In this game, two players (in this case you and the computer), choose one of the three objects suggested at the same time, and present them to each other at the same time.

The following is the win/loss hierarchy:
- Rock: beats scissors, loses to paper
- Paper: beats rock, loses to scissors
- Scissors: beats paper, loses to rock

The scope of this will be a basic input and play against the computer until the game is exited using the word 'exit'.  The win, loss counter will be shown after every game until the game is exited at which the counter will be reset.

Logic:
- Set player and computer counters to 0 ready for being added to
- Ask for the players name, and ask them if they wish to play, which starts a loop if they say yes to play
- In the loop:
    - the computer asks the player to choose one of rock, paper or scissors

Spec revisit - 19/9/23:
* Narrator is computer:
1. Gather name of the human player
2. Choose who goes first - human or computer
3. One function for playing - discrete function or two lines of logic dependent on who wins first choice?
"""

#Imports:
import random
import time

#Counters & Other Initial States:
counter_computer = 0
counter_player = 0
count = 0

choices = ["rock", "paper", "scissors"]

win_loss = {
    "rock": ["paper", "scissors"],
    "paper": ["scissors", "rock"],
    "scissors": ["rock", "paper"] 
}


#Computer asks for Players name and asks if they'd like to play Rock, Paper, Scissors:
player = input("What is your name please? ")
go_play = input(f"Hi {player}, would you like to play today? (yes/no) ").lower()


#On 'No', exit and thank:
if go_play == "no":
    print("Wuss! Seesya and have a good day!")

#On 'yes', lets play & first go:
elif go_play == "yes":
    #Build tension in pre-game: (Code needs to be more Pythonic!)
    print("Let's go play! Please wait while we randomly choose first play!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")


    #Random function to choose player:
    player_choice = random.randint(0,1)

    # Refactor computer choice to randomly choose from dictionary keys:
    computer_first_choice = choices[random.randint(0,2)]

    # Computer plays first:
    if player_choice == 0:
        print("Computer won the toss and gets first play!")
        human_first_choice = input("what is your choice? Rock, paper or scissors? ").lower()

    # Human plays first:
    elif player_choice == 1:
        print(f"Congratulations {player}! You have won the toss!")
        human_first_choice = input("what is your choice? Rock, paper or scissors? ").lower()


# Choice comparison and game winner decided:
if player_choice == 0:
    for key in win_loss:
        print(key)
    # Do we need to loop through? Can't we just match key value, then see if human choice matches value at index 0.

