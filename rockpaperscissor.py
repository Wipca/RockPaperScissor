a = input("Input Username:")
import random

def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            break
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    return user_choice

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    print(a,"chose", user_choice)
    print("Computer chose", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        print(a, "wins!")
    else:
        print("Computer wins!")

print("Welcome to rock paper scissor game!")

user_choice = get_user_choice()
computer_choice = get_computer_choice()
determine_winner(user_choice, computer_choice)
