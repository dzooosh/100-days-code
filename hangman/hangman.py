#!usr/bin/python3

import random
""" 
HANGMAN PROJECT

The game randomly selects a word from a predefined list of words.
The player is prompted to guess a letter, and the game indicates
whether the letter appears in the word or not. The game continues
until the player correctly guesses the word or runs out of attempts.
"""

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

"""

  Todo
    Make dashes based on the number of letters present in the RANDOM word
    Loop continuously till all life is lost or the word is answered correctly
    For any right word replace dash with the letters
"""

# Generate a random word
random_word = random.choice(words)
print(random_word)

# Generate as many blanks as letters in word
for letters in random_word:
  print("_", end=" ")
print("\n")

# Ask the user to guess a letter
guess = input("Guess a letter ?").lower()

# if letter guess in random_word fill the blanks
# else lost one life
for letters in random_word:
  if guess == letters:
    print(f"{guess}", end=" ")
  else:
    print("_", end=" ")
print("\n")
