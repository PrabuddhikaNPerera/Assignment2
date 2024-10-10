#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

# Import necessary modules
import json
import tkinter
from tkinter import messagebox

import requests


# Define the ProgramGUI class for the application interface
class ProgramGUI :
    # Initialize the main window for the GUI
    def __init__(self):
        self.main= tkinter.Tk()
        self.main.title("WordChain Log Viewer") # Set the window title
        self.main.minsize(300,100) # Set the minimum window size

        # Attempt to load log data from a JSON file
        try:
            with open("logs.txt", "r") as file:
                self.logs = json.load(file) # Parse JSON data into a Python object
        # Handle errors for missing or invalid log file
        except (FileNotFoundError,json.JSONDecodeError):
            messagebox.showerror("Error", "Missing/Invalid file") # Show error message
            self.main.destroy() # Close the application
            return # Exit the constructor

        # Initialize the log index for displaying logs
        self.nextLog = 0

        # Set up the layout of the GUI
        self.guiFrame = tkinter.Frame(self.main, padx=30, pady=30) # Create a frame for the widgets
        self.guiFrame.pack()  # Pack the frame into the main window

        # Create labels for displaying log information
        self.logLable = tkinter.Label(self.guiFrame, padx=10, pady=10)
        self.logLable.grid(row=0, column=0, sticky="w")

        self.playerLable = tkinter.Label(self.guiFrame,padx=10, pady=10)
        self.playerLable.grid(row=1,column=0, sticky="w")

        self.ChainLable = tkinter.Label(self.guiFrame,padx=10, pady=10)
        self.ChainLable.grid(row=2,column=0, sticky="w")

        self.statsLabel = tkinter.Label(self.guiFrame, padx=10, pady=10)
        self.statsLabel.grid(row=3, column=0, sticky="w")

        # Create buttons for navigating logs and showing statistics
        self.nextButton = tkinter.Button(self.guiFrame, text="Next Log", command=self.showLog)
        self.nextButton.grid(row=4, column=0,sticky="w")

        self.StatButton = tkinter.Button(self.guiFrame, text="Show Stats", command=self.showStats)
        self.StatButton.grid(row=4, column=1,sticky="w")

        self.wordOfTheDayButton = tkinter.Button(self.guiFrame, text="Word of the Day",command=self.showWordOfTheDay)
        self.wordOfTheDayButton.grid(row=4, column=2, sticky="w", padx=10, pady=10)

        # Display the first log entry when the GUI starts
        self.showLog()
        self.main.mainloop() # Start the GUI event loop

    # Method to display the next log entry
    def showLog(self):
        if self.nextLog < len(self.logs):
            record=self.logs[self.nextLog]
            recordNo = f"Log #: {self.nextLog + 1} {record['date_time']}"
            playerCount = f"Players: {record['players']}  {record['names']}"
            chainLength = f"Chain Length: {record['chain']}"
            stats = f"Nouns: {record['stats']['noun']}, Verbs: {record['stats']['verb']}, Adjectives: {record['stats']['adjective']}"

            # Update the labels with the current log details
            self.logLable.configure(text=recordNo)
            self.playerLable.configure(text=playerCount)
            self.ChainLable.configure(text=chainLength)
            self.statsLabel.configure(text=stats)

            # Move to the next log for the next call
            self.nextLog=self.nextLog+1
        else:
            # Show a warning if there are no more logs to display
            tkinter.messagebox.showwarning("End of File","No more logs to show!")

    # Method to display game statistics
    def showStats(self):
        noGames = len(self.logs) # Count the total number of games logged
        noPlayers= sum(log.get('players', 0) for log in self.logs) # Total players across all logs
        maxChain = max(log.get('chain', 0) for log in self.logs) # Maximum chain length recorded

        # Calculate the average number of players per game
        playerAvg = round(noPlayers/noGames) if noGames > 0 else 0

        # Prepare the statistics message to display
        msg = f"Total games : {noGames}\n Average players per game:{playerAvg}\n Maximum chain length: {maxChain}"
        messagebox.showinfo("WordChain Statistics",msg)

    def showWordOfTheDay(self):
        apiKey = "bnj8kxwj4vm4oe0ri9pwkk8awoug7zqs52r1taf97l8bnbjdv"  #API key from Wordnik
        url = f"https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={apiKey}"

        try:
            response = requests.get(url)
            wordOfTheDay = response.json()
            word = wordOfTheDay['word']
            definition = requests.get(
                f"https://api.wordnik.com/v4/word.json/{word}/definitions?limit=1&api_key={apiKey}")
            meaning = definition.json()
            meaningToShow = meaning[0]['text'] if meaning else "No definition found."

            messagebox.showinfo("Word of the Day", f"Word: {word}\nDefinition: {meaningToShow}")
        except:
            messagebox.showerror("Error", f"Failed to fetch Word of the Day")


# Create an instance of the ProgramGUI class to run the application
gui= ProgramGUI () # create a ProgramGUI object

