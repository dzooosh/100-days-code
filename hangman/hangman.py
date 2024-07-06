#!/usr/bin/python3

""" 
HANGMAN PROJECT

The game randomly selects a word from a predefined list of words.
The player is prompted to guess a letter, and the game indicates
whether the letter appears in the word or not. The game continues
until the player correctly guesses the word or runs out of attempts.
"""


import random
from hangman_words import words
from hangmanpics import HANGMANPICS

# Pick a random word
random_word = random.choice(words)
print(f'Word picked: {random_word}')

# Generate as many blanks as letters in word
# initial list contains the words length in dashes e.g hawk ['_', '_', '_', '_']
# put random word in a list
display = []

# create another list with the right word in a list
# e.g hawk ['h', 'a', 'w', 'k']
word = []
# Number of lives used. Also helps with the hangman pics
LIFE = 0

for letter in random_word:
  word.append(letter)

for letter in range(len(random_word)):
  display += "_"

# continue to loop till answer is right
word_length = len(random_word)

# creating number of lives (6) for trial - after the 6 its game over
while (display != word):
  # Ask the user to guess a letter
  print(HANGMANPICS[LIFE])
  guess = input("Guess a letter(a - z)?").lower()

  # if letter guess in random_word fill the blanks
  # else lose a life
  for position in range(word_length):
    letter = random_word[position]
    if guess == letter:
      display[position] = letter
      
  # check if guess is not present in the display word
  if guess not in display:
    # adding because of the list sequence
    LIFE += 1

  # check if you've used up the 6 guesses
  print(LIFE)

  if LIFE == 6:
    break
  
  print(display)

if display != word:
  print("You Died")
else:
  print("You Win")