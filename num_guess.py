# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/16/2022

# Description: Write a program that prompts the user for an integer that the player (maybe the user, maybe someone
# else) will try to guess. If the player's guess is higher than the target integer, the program should display "too
# high" If the user's guess is lower than the target integer, the program should display "too low" The program should
# use a loop that repeats until the user correctly guesses the integer. Then the program should print how many
# guesses it took.

# asking user to enter number to be guessed.
print("Enter the integer for the player to guess.")
# prompting user to enter number.
number = int(input())
# print message for user to start guessing.
print("Enter your guess.")
# prompting to enter the first guess.
guess = int(input())
# initializing counting action.
count = 1
# creating condition to keep guessing while guessed number is different from target number.
while number != guess:
    # giving guesser clues whether number is too high or too low.
    if guess > number:
        # displaying too high and prompting guesser to enter new number.
        print("Too high - try again: ")
        guess = int(input())
        # counter increased with every try.
        count = count + 1
    if guess < number:
        # displaying too low nad prompting guesser to enter new number.
        print("Too low - try again:")
        guess = int(input())
        # counter increased with every try.
        count = count + 1
# whenever guesser hits targeted value, message is displayed including number of tries.
print("You guessed it in", count, "tries.")
