import random

# opens and reads word options from .txt file
open_words_list = open("hangmanwords.txt", "r")
read_words_list = open_words_list.readlines()

# prints greeting and asks for user's name
print("Welcome to Hangman!\n")
name = input("What is your name? ")

def yes():
    # chooses a word randomly from .txt file and deletes newline
    chosen_word = random.choice(read_words_list).replace('\n', '')

    chosen_word_list = [char for char in chosen_word]

    print("\nOkay, let's start!\n")
    print(len(chosen_word)* "_")

    letters = []
    tries = 15
    while tries > 0:
        print("\n\nYou have " + str(tries) + " tries left.")
        tries -= 1
        letter = input("Guess a letter (in lowercase)! ")

        if letter not in chosen_word:
            print("Wrong!")

        letters.append(letter)

        for char in chosen_word:
            if char in letters:
                print(char, end = "")
            else:
                print("_", end = "")

        if all(elem in letters for elem in chosen_word_list) == True:
            print("\n\nYou won!")
            break

    if all(elem in letters for elem in chosen_word_list) == False:
        print("\n\nYou lost! The answer is " + chosen_word + ".")

# runs the whole game
while True:
    play = input("\nHi, " + name + ", do you want to play Hangman (Y/N)? ")

    if play == "Y":
        yes()

    elif play == "N":
        print("\nToo bad.. See you next time. Bye!")
        break

    else:
        print("\nSorry, I don't understand. Please try again.")