#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

# Import necessary modules
import json
import random
import requests
from datetime import datetime

# Function to get the number of players for the game
def inputNumber(prompt):
    while True:
        try:
            number = int(input(prompt)) # Prompt user for input and convert to integer
            if number < 2:
                print("Error: The number must be greater than of equal 2.") # Check if the number is greater than or equal 2
            else:
                return number # Return valid player count
        except ValueError:
            print("Invalid input. Please enter a valid integer.") # Handle non-integer inputs

# Function to get a valid word input from the player
def inputWord(prompt):
    while True:
        word = input(prompt).strip() # Prompt user for a word and strip any whitespace
        if word.isalpha() and len(word) > 0:  # Validate input to be letters only and non-empty
            return word # Return valid word
        print("Invalid input. Please enter a valid word containing only letters.") # Error message for invalid input

# Function to log game details to a JSON file
def logGame(noPlayers, playerNames, chain,stats):
    log_entry = {
        "players": noPlayers,
        "names": playerNames,
        "chain": chain,
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "stats": stats
    }
    # Attempt to read existing logs
    try:
        with open("logs.txt", "r") as file:
            logs = json.load(file) # Load existing game logs
    except (FileNotFoundError, json.JSONDecodeError):
        logs = [] # If file not found or JSON is invalid, initialize logs as an empty list

    logs.append(log_entry) # Append new log entry to the logs list

    # Write updated logs back to the file
    with open("logs.txt", "w") as file:
        json.dump(logs, file, indent=4)
        file.close()
        print("Game log saved")

# Function to check the validity of a word using the Wordnik API
def checkWordnik(word, wordType, apiKey):
    # Construct API request URL
    url = f"https://api.wordnik.com/v4/word.json/{word}/definitions?limit=5&partOfSpeech={wordType}&api_key={apiKey}"
    response = requests.get(url) # Send GET request to the Wordnik API
    return response.json() # Return the JSON response

def getRandomWord(apiKey):
    url = f"https://api.wordnik.com/v4/words.json/randomWord?api_key={apiKey}"
    response = requests.get(url)
    return response.json()

def main():
    #Define variables
    chain = 0
    wordTypes = ["noun","verb","adjective"]
    playerNames = []
    usedWords = []
    apiKey = "bnj8kxwj4vm4oe0ri9pwkk8awoug7zqs52r1taf97l8bnbjdv"  #API key from Wordnik
    stats = {"noun": 0, "verb": 0, "adjective": 0} #Dictionary

    #Welcome message
    print("Welcome to WordChain!")

    # Get number of players
    numberofplayers = inputNumber("Enter the number of players (minimum 2): ")
    print (numberofplayers)

    # Get player names
    while len(playerNames) < numberofplayers:
        name = inputWord(f"Enter the name for player {len(playerNames) + 1}: ")
        if name not in playerNames:
            playerNames.append(name)
        else:
            print("That name is already entered. Please choose a different name.")

    print("\nLet's Start the Game!")

    #StartGame
    firstLetter = random.choice('abcdefghijklmnopqrstuvwxyz') # Randomly select word type for current turn
    currentPlayer = 0
    while True:
        currentWordType = random.choice(wordTypes)
        print(f"\n{playerNames[currentPlayer]} is up next. \nEnter a {currentWordType} starting with '{firstLetter}':")

        word = inputWord("Your word: ")
        #print (word)

        # Check the first letter of the input word and if the word was used before
        if word[0] != firstLetter or word in usedWords:
            print(f"\nInvalid word! Word chain is broken with your input '{word}'.")
            break

        # Check if the word is recognized
        definitions = checkWordnik(word, currentWordType, apiKey)

        # Initialize list to store word definitions
        meaning = []
        # Attempt to collect definitions from API response
        try:
            for definition in definitions:
                meaning.append({definition['text']}) # Add definition text to the meanings list
        except:
            print(f"\n'{word}' is not recognized as a {currentWordType}. The game is over.")
            break # Exit loop if there's an error

        # Check if any meanings were found
        if meaning:
            print(f"\nGood job, {playerNames[currentPlayer]}! Definitions:")
            print(f"{meaning}")
            stats[currentWordType] += 1  # Increment count for the word type
        else:
            print(f"\n'{word}' is not recognized as a {currentWordType}. The game is over.")
            break

        # Valid word, update game state
        chain += 1 # Increment the word chain length
        usedWords.append(word) # Add the word to the list of used words
        firstLetter= word[-1] # Update starting letter for next player


        print(f"\nThe word chain is now {chain} links long")

        # Move to the next player
        currentPlayer = (currentPlayer + 1) % numberofplayers

    # Log the game
    print(f"Final chain length: {chain}")
    logGame(numberofplayers,playerNames,chain,stats)

    # Get a random word and its definition
    randomWordData = getRandomWord(apiKey)
    randomWord = randomWordData['word']
    randomWordDef = checkWordnik(randomWord, "noun", apiKey)  # Check definition as a noun

    if randomWordDef:
        print(f"\nRandom Word: {randomWord}")
        print("Definitions:", [definition['text'] for definition in randomWordDef])
    else:
        print(f"\nCouldn't find definitions for the random word '{randomWord}'.")

main()