import random
import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    return list(secret_word) == list(letters_guessed)

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = list(string.ascii_lowercase)
    for l in letters_guessed:
        letters_left.remove(l)
    return "".join(letters_left)


def print_image(IMG, rem_lives):
    print(IMG[8-rem_lives])


def isValid(input_character):
    """condition : 
      * input length == 1
      * must be character from a-z
    return :
      true or false"""
    return len(input_character) == 1 or input_character not in string.ascii_lowercase


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    hint_used = False

    remaining_lives = 8

    while remaining_lives:
        print("\nRemaining lives : ", remaining_lives)

        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} \n".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if not isValid(letter):
            print("The input is not valid")
            continue

        elif letter == "hint" and hint_used:
            print("You have used your hint")
            continue

        elif letter == "hint" and not hint_used:
            hint_used = True
            # taking all chars in secret_word
            chrs = set(secret_word)
            # removing chars in letters_guessed from chrs which gives the remaining characters to be entered
            for i in letters_guessed:
                chrs.remove(i)

            # getting random character from the remaining characters to be entered
            letter = random.choice(list(chrs))

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            print_image(IMAGES, remaining_lives)
            letters_guessed.append(letter)
            print("")
            remaining_lives -= 1


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
