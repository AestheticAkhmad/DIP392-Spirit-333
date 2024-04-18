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
        if re.match(self.pattern, self.player1.name):
            print(f"Player 1: {self.player1.name}")
        else:
            print("Invalid username for player 1. Please just use alphabet and numbers")
        
        if re.match(self.pattern, self.player2.name):
            print(f"Player 2: {self.player2.name}")
        else:
            print("Invalid username for player 2. Please just use alphabet and numbers")
    
    def InitPlayerNames(self):
        self.player1.name = self.player1_entry.get()
        self.player2.name = self.player2_entry.get()

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

    def CheckPlayerNames(self):
        pass