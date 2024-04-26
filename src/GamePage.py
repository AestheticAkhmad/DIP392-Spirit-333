import tkinter as tk
from tkinter import ttk
from List_of_words import word_hints
import random

class GamePage:
    def __init__(self, main_window) -> None:
        self.game_frame = ttk.Frame(main_window)
        self.game_frame.grid(row=0, column=0, sticky='nsew')
        self.letter_tiles = list()
        self.hint_label = None
        self.rule_label = None
        self.playing_word = ""
        self.hint = ""
        self.word_indices = dict()
        self.playing_letter = ""

        self.open_game_window()
        self.ReadWordAndHint()
        main_window.bind("<Key>", self.GetPressedKey)
        self.game_frame.tkraise()

    def GetRandomNumber(self):
        return random.randint(0, 39)
    
    def FindLetter(self, letter):
        if letter in self.word_indices:
            return True, self.word_indices[letter]
        return False, []

    def SplitPlayingWord(self):
        for i, k in enumerate(self.playing_word):
            if k not in self.word_indices:
                self.word_indices[k] = [i]
            else:
                self.word_indices[k].append(i)

        print(self.word_indices)

    def ReadWordAndHint(self):
        random_number = self.GetRandomNumber()
        self.playing_word = list(word_hints[random_number].keys())[0].upper()
        self.hint = list(word_hints[random_number].values())[0]
        self.hint_label.config(text="Hint: "+ self.hint)

        index = len(self.playing_word)

        while index < len(self.letter_tiles):
            self.letter_tiles[index].pack_forget()
            index += 1

        self.SplitPlayingWord()

        print(self.playing_word, "\n", self.hint)

    def GetLetterInput(self):
        letter = self.playing_letter
        if len(letter) == 1 and letter.isalpha():
            print(letter)
        else:
            print("Letter must be alphabetic without numbers and special characters.")
    
    def ShowFoundLetters(self, indices):
        for i in indices:
            self.letter_tiles[i].config(text=f" {self.playing_word[i]} ")

    def GetPressedKey(self, event):
        current_letter = event.keysym
        if current_letter == "Return":
            found, letters = self.FindLetter(self.playing_letter)
            if found == True:
                self.ShowFoundLetters(letters)

        elif current_letter.isalpha():
            self.playing_letter = current_letter.upper()

    def open_game_window(self):
        # Top Frame
        top_frame = ttk.Frame(self.game_frame)

        # Creating 12 tiles for letters
        tiles_frame = ttk.Frame(top_frame)
        tiles_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=(20, 10))
        for i in range(12):
            tile_label = ttk.Label(tiles_frame, text="    ", font=('Arial', 50), borderwidth=1, relief="raised")
            tile_label.pack(side="left", padx=2)
            self.letter_tiles.append(tile_label)

        # Home button
        home_button = tk.Button(top_frame, text="Home")
        home_button.grid(row=0, column=1, sticky='nse', padx=10, pady=(20, 10))
        home_button.config(height=2, width=10)

        exit_button = tk.Button(top_frame, text="Exit")
        exit_button.grid(row=0, column=2, sticky='nse', padx=10, pady=(20, 10))
        exit_button.config(height=2, width=10)

        # Bottom frame
        bottom_frame = ttk.Frame(self.game_frame)

        # Hint label
        bottom_left_frame = ttk.Frame(bottom_frame)
        self.hint_label = tk.Label(bottom_left_frame, text="", font=('Arial', 26))
        self.hint_label.grid(row=0, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

        self.rule_label = tk.Label(bottom_left_frame, text="Rule: press alphabetic letter and Enter key.", font=('Arial', 16))
        self.rule_label.grid(row=1, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

        # Bottom middle frame
        bottom_middle_frame = ttk.Frame(bottom_frame)

        # Wheel
        #

        # Placeholder for wheel bonus
        bonus_frame = ttk.Frame(bottom_middle_frame, borderwidth=2, relief="sunken", width=200, height=100)
        bonus_frame.grid(row=1, column=0, sticky='nsew')

        # Bottom right frame
        bottom_right_frame = ttk.Frame(bottom_frame)

        # Player scores labels
        player1_score_label = tk.Label(bottom_right_frame, text="Player 1 Score: 0")
        player1_score_label.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        player2_score_label = tk.Label(bottom_right_frame, text="Player 2 Score: 0")
        player2_score_label.grid(row=1, column=0, sticky='nsew', padx=0, pady=0)

        # Player's turn label
        turn_label = tk.Label(bottom_right_frame, text="Player 1's Turn", bg='blue', fg='white')
        turn_label.grid(row=2, column=0, sticky='nsew', padx=0, pady=0)

        # Rotate button
        rotate_button = tk.Button(bottom_right_frame, text="Rotate")
        rotate_button.grid(row=3, column=0, sticky='nsew', padx=0, pady=0)


        top_frame.grid(row=0, column=0, sticky='nsew', pady=(30, 30))
        bottom_frame.grid(row=1, column=0, sticky='nsew')
        bottom_left_frame.grid(row=1, column=0, sticky='nsew')
        bottom_middle_frame.grid(row=1, column=1, sticky='nsew')
        bottom_right_frame.grid(row=1, column=2, sticky='nsew')

        
