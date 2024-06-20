""" 
Love Calculator
This calculates the number of letter in "TRUE LOVE" that is present in your name and 
your partner's name and tells you how compatible you are with the other person.
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1.upper() + name2.upper()

# concatenate the sum as strings
# convert result back to number

true_count = 0
love_count = 0

# 2 for loops: 1 for true and 1 for love
# count if letters 'T'R'U'E' can be found in combined names
for lt in combined_string:
    if (lt == 'T') or (lt == 'R') or (lt == 'U') or (lt == 'E'):
        true_count += 1

# count if letters 'L'O'V'E' can be found 
for lt in combined_string:
    if (lt == 'L') or (lt == 'O') or (lt == 'V') or (lt == 'E'):
        love_count += 1

love_score = int(str(true_count) + str(love_count))

# print(love_score) # debug: check if output is correct

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
