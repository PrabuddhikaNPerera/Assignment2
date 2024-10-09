#Student Name : Prabuddhika Panawalage
#Student ID : 10609924

import json
import tkinter
from email.utils import make_msgid
from tkinter import messagebox


class ProgramGUI : # define a ProgramGUI class
    def __init__(self):
        self.main= tkinter.Tk()
        self.main.title("WordChain Log Viewer")
        self.main.minsize(400,300)


        try:
            with open("logs.txt", "r") as file:
                self.logs = json.load(file)

        except (FileNotFoundError,json.JSONDecodeError):
            messagebox.showerror("Error", "Missing/Invalid file")
            self.main.destroy()
            return

        self.nextLog = 0
# Layout
        self.guiFrame = tkinter.Frame(self.main, padx=30, pady=30)
        self.guiFrame.pack()

        self.logLable = tkinter.Label(self.guiFrame, text="Game Details")
        self.logLable.grid(row=0, column=0, sticky="w")

        self.playerLable = tkinter.Label(self.guiFrame,padx=10, pady=10)
        self.playerLable.grid(row=1,column=0, sticky="w")

        self.ChainLable = tkinter.Label(self.guiFrame,padx=10, pady=10)
        self.ChainLable.grid(row=2,column=0, sticky="w")

        self.nextButton = tkinter.Button(self.guiFrame, text="Next Log", command=self.showLog)
        self.nextButton.grid(row=3, column=0,sticky="w")

        self.StatButton = tkinter.Button(self.guiFrame, text="Show Stats", command=self.showStats)
        self.StatButton.grid(row=4, column=0,sticky="w")

        self.showLog()
        self.main.mainloop()

    def showLog(self):
        if self.nextLog < len(self.logs):
            record=self.logs[self.nextLog]
            recordNo= f"Log #: {self.nextLog + 1}"
            playerCount = f"Players: {record['players']}"
            chainLength = f"Chain Length: {record['chain']}"

            self.logLable.configure(text=recordNo)
            self.playerLable.configure(text=playerCount)
            self.ChainLable.configure(text=chainLength)

            self.nextLog=self.nextLog+1
        else:
            tkinter.messagebox.showwarning("No more logs to show!")


    def showStats(self):
        noGames = len(self.logs)
        noPlayers= sum(log.get('players', 0) for log in self.logs)
        maxChain = max(log.get('chain', 0) for log in self.logs)

        playerAvg = round(noPlayers/noGames) if noGames > 0 else 0

        msg = f"Total games : {noGames}\n Average players per game:{playerAvg}\n Maximum chain length: {maxChain}"
        messagebox.showinfo("WordChain Statistics",msg)

gui= ProgramGUI () # create a ProgramGUI object

