import random

print("Welcome to the Guess the Number game!")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Initialize variables
guess = 0
tries = 0

# Start the game loop
while guess != number:
    # Get the player's guess
    guess = int(input("Enter your guess: "))
    
    # Increment the number of tries
    tries += 1
    
    # Check if the guess is too high or too low
    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")

# The game is over
print("Congratulations! You guessed the correct number in {} tries.".format(tries))
