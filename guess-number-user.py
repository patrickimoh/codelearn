import random

def computer_guess(x):
    low = 1 # lower number
    high = x # higher number
    feedback = " "
    while feedback != "c" and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"The computer guessed your number, {guess}, correctly")

computer_guess(10)