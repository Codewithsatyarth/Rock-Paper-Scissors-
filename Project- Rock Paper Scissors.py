# Project 7: Rock, Paper, Scissors Game
import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)

# Taking user's input
user = input("Enter rock, paper, or scissors:").lower()
print(f"Computer choices: {computer}")
if user == computer:
    print("It's a tie! . Draw🤝!") 

elif (user == "rock" and computer == "scissors"):
    print("rock smashes scissors! you win! 🎉")     
    print("You win! 🎉")

elif (user == "paper" and computer == "rock"):
    print("paper covers rock! you win! 🎉")
    print("You win! 🎉")

elif (user == "scissors" and computer == "paper"):
    print("scissors cut paper! you win! 🎉")
    print("You win! 🎉")

else:
    print("You lose! 😢")
    print(f"{computer} beats {user}! You lose! 😢 , Computer Wins🎉!")

print("Game Over. Thanks for playing!")

# End of the game

# If you love tis game then please give a star⭐ to this repository on GitHub!
# GitHub Repository Link:
# 