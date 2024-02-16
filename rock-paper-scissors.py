import random

# Initialize counters for the user's wins, computer's wins, and tie games
user_wins = 0
computer_wins = 0
tie_games = 0

# List of valid game options
options = ["rock", "paper", "scissors"]

# Function to play a single round of the game
def play_round(user_input, computer_pick):
    # Check for a tie condition
    if user_input == computer_pick:
        global tie_games
        tie_games += 1  # Increment tie games counter
        return "It's a tie!"
    # Check for conditions where the user wins
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        global user_wins
        user_wins += 1  # Increment user's win counter
        return "You won!"
    else:
        # If not a tie or a user win, the computer wins
        global computer_wins
        computer_wins += 1  # Increment computer's win counter
        return "You lost!"

# Main game loop
while True:
    # Prompt the user for input and convert it to lowercase for consistency
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    # Check if the user wants to quit the game
    if user_input == "q":
        break
    # Validate the user's input
    if user_input not in options:
        # Inform the user of invalid input and prompt for another attempt
        print("Invalid input. Please choose Rock, Paper, Scissors, or Q to quit.")
        continue
    # Generate a random choice for the computer
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    
    # Play a round with the user's and computer's choices and print the result
    print(play_round(user_input, computer_pick))

# After exiting the game loop, print the final results
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print(f"Tie games: {tie_games}.")
print("Goodbye!")  # Farewell message
