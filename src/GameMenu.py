import tkinter as tk
from tkinter import ttk
import re

class Player:
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score
        
class GameMenu:
    def __init__(self, main_window) -> None:
        self.player1 = Player("", 0)
        self.player2 = Player("", 0)
        self.player1_entry = None
        self.player2_entry = None
        self.window = main_window
        self.menu_frame = ttk.Frame(self.window)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.pattern = r"^(?=.*[A-Za-z])[A-Za-z0-9]{3,16}$"
        self.info_label = None

        self.CreateMenu()
        
    def InitPlayers(self):
        pass

    def GetLeftWidth(self):
        return 500
    
    def GetRightWidth(self):
        return 5
    
    def GetTopHeight(self):
        return 240
    
    def PrecheckInput(self):
        both_are_valid = True
        error_message = ""
        if not re.match(self.pattern, self.player1.name):
            error_message = "Invalid name for Player 1.\nPlease use only numbers and English lettes.\n"
            both_are_valid = False
        
        if not re.match(self.pattern, self.player2.name):
            error_message += "Invalid name for Player 2.\nPlease use only numbers and English lettes."
            both_are_valid = False

        if not both_are_valid:
            self.info_label.config(text=error_message)

        if both_are_valid:
            self.StartGame()

    def InitPlayerNames(self):
        self.player1.name = self.player1_entry.get()
        self.player2.name = self.player2_entry.get()

    def StartGame(self):
        print("STARTED THE GAME")

    def InitStart(self):
        self.InitPlayerNames()
        self.PrecheckInput()

    def CreateMenu(self):
        # Creating labels
        player1_label = tk.Label(self.menu_frame, text="First player name:")
        player1_label.grid(row=0, column=0, sticky='e', 
                           padx=(self.GetLeftWidth(), self.GetRightWidth()), 
                           pady=(self.GetTopHeight(), 0))

        self.player1_entry = tk.Entry(self.menu_frame)
        self.player1_entry.grid(row=0, column=1, sticky='w', 
                           padx=(self.GetRightWidth(), self.GetLeftWidth()), 
                           pady=(self.GetTopHeight(), 0))

        player2_label = tk.Label(self.menu_frame, text="Second player name:")
        player2_label.grid(row=1, column=0, 
                           padx=(self.GetLeftWidth(), self.GetRightWidth()), 
                           pady=10)

        self.player2_entry = tk.Entry(self.menu_frame)
        self.player2_entry.grid(row=1, column=1, 
                           padx=(self.GetRightWidth(), self.GetLeftWidth()), 
                           pady=10)

        # Creating start button
        start_button = tk.Button(self.menu_frame, text="Start Game", command=self.InitStart)
        start_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        start_button.config(height=2, width=20)

        # Notification label
        self.info_label = tk.Label(self.menu_frame, text="Please, use English letters and numbers.", fg="red")
        self.info_label.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

    def CheckPlayerNames(self):
        pass