"""a deductive logic game where you must guess
a number based on clues
"""

import random

NUM_DIGITS = 3 # (!) try setting this to 1 or 10
MAX_GUESS = 10 # (!) try setting this to 1 or 100


def main():
    print('''Bagels. a deductive logic game.
    by Muhammad hamissi
        
    I am thinking of a {}-digit number with no repeated digits.
    try to guess what it is. here are some clues:
    when I say: that means:
    Pico      one digit is correct but in the wrong position.
    Fermi     one digit is correct and in the right position. 
    Bagels    no digit is correct. 
    
    for example, if the secret number was 248 and your guess was
    843, the clues would be Fermi Pico 
    '''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print("I have thought up a number. ")
        print("you have {} guesses to get it. ".format(MAX_GUESS))

        num_Guesses = 1
        while num_Guesses <= MAX_GUESS:
            guess = ''
            # keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(num_Guesses))
                guess = input('>')
            clues = getClues(guess, secretNum)
            print(clues)
            num_Guesses += 1

            if guess == secretNum:
                break
            if num_Guesses > MAX_GUESS:
                print("you ran out of guesses. ")
                print("the answer was {}. ".format(secretNum))

        # ask player if they want to play again.
        print("do you want to play again? (yes or no )")
        if not input(" > ").lower().startswith("y"):
            break
    print("thanks for playing!")

def getSecretNum():
    """
    returns a string made up of NUM_DIGITS unique random digits.
    """
    numbers = list('0123456789') # create a list of digits 0 to 9
    random.shuffle(numbers) # shuffle them into a random order

    # get the first NUM_DIGITS digits in the list for the secret number:

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """
    returns a string with the pico, fermi, bagels clues for a gues
    and secret number pair.
    """
    if guess == secretNum:
        return 'You got it!'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('fermi')
            # a correct digit is in the correct place
        elif guess[i] in secretNum:
            clues.append('pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)

if __name__ == '__main__':
    main()





