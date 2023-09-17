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
    - 
"""

#Imports:
import random
import time

#Counters & Other Initial States:
counter_computer = 0
counter_player = 0
count = 0


#Computer asks for Players name and asks if they'd like to play Rock, Paper, Scissors:
player = input("What is your name please? ")
go_play = input(f"Hi {player}, would you like to play today? (yes/no) ").lower()


#On 'No', exit and thank:
if go_play == "no":
    print("Wuss! Seesya and have a good day!")

#On 'yes', lets play:
elif go_play == "yes":
    # print(go_play)
    print("Let's go play! Please wait while we randomly choose first play!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    player_choice = random.randint(0,1)
    if player_choice == 0:
        print("Computer gets first play")
    elif player_choice == 1:
        print(f"Congratulations {player}! You have won the toss!")




