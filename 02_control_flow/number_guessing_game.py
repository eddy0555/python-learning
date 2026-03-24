import random

# Generate random number
secret_num = random.randint(1,10)

# Initiate guess variable
guess_num = None

set_guess = 0

#Prompt number guessing game question
print ("Try to guess the secret number that is between 1 and 100!")

while guess_num != secret_num:

    guess_num = int(input("Enter your guess: "))
    set_guess += 1

    if guess_num < secret_num:
        print ("Too Low bro")
    
    elif guess_num > secret_num:
        print ("Too high bro")
    
    else:print("Nice! Good Job Stupid")

print("Total guesses was:",set_guess)