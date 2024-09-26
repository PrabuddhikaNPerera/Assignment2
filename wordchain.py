#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

import random
import requests


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


def checkWordnik(word, wordType, apiKey):
    url=f'http://api.wordnik.com/v4/words.json/randomWord?api_key={apiKey}'
    url = f"https://api.wordnik.com/v4/word.json/{word}/definitions?limit=5&partOfSpeech={wordType}&api_key={apiKey}"
    response = requests.get(url)
    return response.json()


def main():
    #Define variables
    chain = 0
    wordTypes = ["noun","verb","adjective"]
    playerNames = []
    usedWords = []
    apiKey = "bnj8kxwj4vm4oe0ri9pwkk8awoug7zqs52r1taf97l8bnbjdv"  #API key from Wordnik

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
    firstLetter = random.choice('abcdefghijklmnopqrstuvwxyz')
    currentPlayer = 0
    while True:
        currentWordType = random.choice(wordTypes)
        print(f"{playerNames[currentPlayer]} is up next. \nEnter a {currentWordType} starting with '{firstLetter}':")

        word = inputWord("Your word: ")
        print (word)

        # Check the first letter of the input word and if the word was used before
        if word[0] != firstLetter or word in usedWords:
            print(f"Invalid word! Word chain is broken with your input '{word}'.")
            break

        # Check if the word is recognized
        definitions = checkWordnik(word, currentWordType, apiKey)
        if not definitions:
            print(f"'{word}' is not recognized as a {currentWordType}. The game is over.")
            break



main()