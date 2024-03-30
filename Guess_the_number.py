import random

def getRandomNumber():
    """
    Generate a random number between 1 and 100.

    Returns:
    int: A random number between 1 and 100.
    """
    return random.randrange(1, 100)

def giveHint(number, guess):
    """
    Provide a hint based on the user's guess.

    Args:
    number (int): The secret number.
    guess (int): The user's guess.

    Returns:
    str: A hint indicating whether the guess is "Cold", "Hot", or "Right".
    """
    if guess > (number + 10) or guess < (number - 10):
        return "Cold"
    elif number == guess:
        return "Right"
    else:
        return "Hot"

def runGuess():
    """
    Run the guess the number game.
    """
    secretNumber = getRandomNumber()
    # Update the code below
    while True:
        user_guess = int(input("Enter a number between 1 and 100: "))
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it Right!")
            break
        else:
            print(hint)
            
if __name__ == '__main__':
    runGuess()