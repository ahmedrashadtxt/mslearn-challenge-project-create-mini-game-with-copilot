#Create a rock-paper-scissors game with the computer. Validation should be done for the input. The game should continue until the user decides to quit. The user should be able to see the score of the game.
def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        if user_input == 'q':
            return None
        elif user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    import random
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "user"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "user"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "user"
    else:
        return "computer"
    
# Initialize scores
user_score = 0
computer_score = 0
# Game loop
while True:
    # Get user choice
    user_choice = get_user_choice()
    
    # Check if user wants to quit
    if user_choice is None:
        break
    
    # Get computer choice
    computer_choice = get_computer_choice()
    print(computer_choice)
    
    # Determine winner
    winner = determine_winner(user_choice, computer_choice)
    print("Winner: ", winner)
        
    # Update scores
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    
# Determine final winner
if user_score > computer_score:
    final_winner = "User"
elif user_score < computer_score:
    final_winner = "Computer"
else:
    final_winner = "Tie"
    
print("Final Score:")
print("User: ", user_score)
print("Computer: ", computer_score)
print("Final Winner: ", final_winner)