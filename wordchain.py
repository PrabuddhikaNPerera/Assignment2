#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

import random

#Function to get number of players
def inputNumber(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 2:
                print("Error: The number must be greater than of equal 2.") # Check if the number is greater than or equal 2
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def inputWord(prompt):
    while True:
        word = input(prompt).strip()
        if word.isalpha() and len(word) > 0:  # Check if input is consists entirely of letters and is at least one character long
            return word
        print("Invalid input. Please enter a valid word containing only letters.")


def main():
    #Define variables
    chain = 0
    wordTypes = ["noun","verb","adjective"]
    playerNames = []
    usedWords = []
    api_key = "bnj8kxwj4vm4oe0ri9pwkk8awoug7zqs52r1taf97l8bnbjdv"  #API key from Wordnik

    #Welcome message
    print("Welcome to WordChain!")

    # Get number of players
    numberofplayers = inputNumber("Enter the number of players (minimum 2): ")
    print (numberofplayers)

    # Get player names
    for i in range(numberofplayers):
        name = inputWord(f"Enter the name for player {i + 1}: ")
        playerNames.append(name)

    print("\nLet's Start the Game!")

    #StartGame
    first_letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    currentPlayer = 0
    while True:
        current_word_type = random.choice(wordTypes)
        print(f"{playerNames[currentPlayer]} is up next. \nEnter a {current_word_type} starting with '{first_letter}':")

        word = inputWord("Your word: ")
        print (word)


main()