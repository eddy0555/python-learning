import random

# Generate random number
secret_num = random.randint(1,10)

# Initiate guess variable
guess_num = None

set_guess = 0

#Prompt number guessing game question
print ("Try to guess the secret number that is between 1 and 10!")

while guess_num != secret_num:

    try: 
        guess_num = int(input("Enter your guess: "))
        set_guess += 1

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
        
    if guess_num < secret_num:
        print ("Too Low bro")
    
    elif guess_num > secret_num:
        print ("Too high bro")
    
    else:print("Nice! Good Job Stupid")

print("Total guesses was:",set_guess)