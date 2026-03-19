import random

# Generate random number
secret_num = random.randint(1,10)

# Initiate guess variable
guess_num = None

#Prompt number guessing game question
print ("Try to guess the secret number that is between 1 and 100!")

while guess_num != secret_num:

    guess_num = int(input("Enter your guess: "))
    
print("Nice! Good Job Stupid")

"""

WHILE guess is not equal to secret_number:

    Ask user to enter a guess
    Convert input to a number
    Store it in guess

    IF guess is less than secret_number:
        Display "Too low"

    ELSE IF guess is greater than secret_number:
        Display "Too high"

    ELSE:
        Display "Correct! You guessed it"

END WHILE

END
"""