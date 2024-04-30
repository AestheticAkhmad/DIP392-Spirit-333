import tkinter as tk
from tkinter import ttk
from List_of_words import word_hints
from Wheel import Wheel
import random
import collections

class GamePage:
    def __init__(self, main_window, player1, player2) -> None:
        self.game_frame = ttk.Frame(main_window)
        self.game_frame.grid(row=0, column=0, sticky='nsew')
        self.letter_tiles = list()
        self.hint_label = None
        self.rule_label = None
        self.playing_word = ""
        self.hint = ""
        self.word_indices = dict()
        
        self.player1 = player1
        self.player2 = player2
        self.player_turn = self.GetRandomPlayerTurn()
        self.wheel = None
        self.can_move = True
        self.current_bonus_label = None
        self.current_input_letter = None
        self.current_input_word = None
        self.word_start_idx = 0
        self.selected_option = "L"
        self.guessing_input_word = collections.deque()
        self.guessing_input_letter = ""

        self.InitGameWindow()
        self.ReadWordAndHint()
        main_window.bind("<Key>", self.GetPressedKey)
        self.game_frame.tkraise()

    def GetRandomNumber(self):
        return random.randint(0, 39)
    
    def GetRandomPlayerTurn(self):
        rand_num = random.randint(1, 2)
        if rand_num == 1:
            return self.player1.name
        else:
            return self.player2.name
    
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

        self.word_start_idx = int((12 - len(self.playing_word))/2)

        start = self.word_start_idx
        if len(self.playing_word) % 2 == 0:
            end = 12 - start
        else:
            end = 12 - start - 1

        while start < end:
            self.letter_tiles[start].config(bg='lightblue')
            start += 1
        

        self.SplitPlayingWord()

        print(self.playing_word, "\n", self.hint)
    
    def ShowFoundLetters(self, indices):
        for i in indices:
            self.letter_tiles[i + self.word_start_idx].config(text=f"{self.playing_word[i]}")

    def GetPressedKey(self, event):
        current_letter = event.keysym
        if current_letter == "Return":
            found, letters = self.FindLetter(self.guessing_input_letter)
            if found == True:
                self.ShowFoundLetters(letters)
                self.UpdatePlayerScore()
            else:
                self.ChangePlayerTurn()

        elif current_letter == "BackSpace":
            if len(self.guessing_input_word) > 0:
                self.guessing_input_word.pop()
            self.guessing_input_letter = ""

        elif current_letter.isalpha():
            if len(self.guessing_input_word) >= len(self.playing_word):
                self.guessing_input_word.popleft()
            
            self.guessing_input_letter = current_letter.upper()
            self.guessing_input_word.append(self.guessing_input_letter)

        self.current_input_letter.config(text=f"{self.guessing_input_letter}")
        self.current_input_word.config(text=f"{''.join(self.guessing_input_word)}")
        
        

        # "BackSpace" - delete event
        print(current_letter)

    def UpdatePlayerScore(self):
        pass
    
    def ChangePlayerTurn(self):
        pass

    def StartWheelRotation(self):
        if self.can_move == True:
            self.can_move = False
            self.current_bonus_label.config(text=f'Rotating...')
            def SetBonusLabel(angle):
                bonus = self.wheel.GetBonus(angle)
                self.current_bonus_label.config(text=f'{bonus}')

            self.wheel.RotateWheel(callback=SetBonusLabel)

    def InitTopFrame(self):
        # Top Frame
        top_frame = ttk.Frame(self.game_frame)

        # Creating 12 tiles for letters
        tiles_frame = ttk.Frame(top_frame)
        tiles_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=(20, 10))

        for i in range(12):
            tile_label = tk.Label(tiles_frame, text=" ", 
                                  font=('Arial', 50),
                                  fg='black',
                                  borderwidth=1, 
                                  relief="raised", 
                                  width=2, 
                                  anchor='center',
                                  bg='#5A5A5A')
            tile_label.pack(side="left", padx=2)
            self.letter_tiles.append(tile_label)

        # Home button
        home_button = tk.Button(top_frame, text="Home")
        home_button.grid(row=0, column=1, sticky='nse', padx=10, pady=(20, 10))
        home_button.config(height=2, width=10)

        exit_button = tk.Button(top_frame, text="Exit")
        exit_button.grid(row=0, column=2, sticky='nse', padx=10, pady=(20, 10))
        exit_button.config(height=2, width=10)
        
        top_frame.grid(row=0, column=0, sticky='nsew', pady=(30, 30))

    def GenerateBottomLeftFrame(self, bottom_frame):
        # Hint label
        bottom_left_frame = ttk.Frame(bottom_frame)
        self.hint_label = tk.Label(bottom_left_frame, text="", font=('Arial', 26))
        self.hint_label.grid(row=0, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

        self.rule_label = tk.Label(bottom_left_frame, text="Rule: press alphabetic letter and Enter key.", font=('Arial', 16))
        self.rule_label.grid(row=1, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

        bottom_left_frame.grid(row=1, column=0, sticky='nsew')

    def GenerateBottomMiddleFrame(self, bottom_frame):
        # Bottom middle frame
        bottom_middle_frame = ttk.Frame(bottom_frame)

        # Wheel
        wheel_frame = ttk.Frame(bottom_middle_frame)
        self.wheel = Wheel(wheel_frame)
        wheel_frame.grid(row=0, column=0, sticky="nsew")

        # Placeholder for wheel bonus
        bonus_frame = ttk.Frame(bottom_middle_frame, borderwidth=2, relief="sunken", width=200, height=100)
        bonus_frame.grid(row=1, column=0, sticky='nsew')
        self.current_bonus_label = ttk.Label(bonus_frame, text="No bonuses.", font=('Fixedsys', 30, "bold"))
        self.current_bonus_label.grid(row=0,column=0, sticky='nsew')

        # Rotate button
        self.rotate_button = tk.Button(bottom_middle_frame, text="Rotate Wheel")
        self.rotate_button.config(command=lambda: self.StartWheelRotation())
        self.rotate_button.grid(row=2, column=0, sticky='nsew', padx=0, pady=0)

        bottom_middle_frame.grid(row=1, column=1, sticky='nsew')

    def GenerateBottomRightFrame(self, bottom_frame):
        # Bottom right frame
        bottom_right_frame = ttk.Frame(bottom_frame)

        # Player scores labels
        player1_score_label = tk.Label(bottom_right_frame, text=f"{self.player1.name} Score: 0")
        player1_score_label.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        player2_score_label = tk.Label(bottom_right_frame, text=f"{self.player2.name} Score: 0")
        player2_score_label.grid(row=1, column=0, sticky='nsew', padx=0, pady=0)

        # Player's turn label
        turn_label = tk.Label(bottom_right_frame, text=f"{self.player_turn}'s Turn", bg='blue', fg='white')
        turn_label.grid(row=2, column=0, sticky='nsew', padx=0, pady=0)

        # Guess placements
        self.selected_option = tk.StringVar()

        guess_choice_frame = ttk.Frame(bottom_right_frame)
        guess_choice_frame.grid(row=3, column=0, sticky='nsew', padx=0, pady=(10, 10))

        current_letter_label = tk.Label(guess_choice_frame, text=f"Current entered letter:")
        current_letter_label.grid(row=0, column=1, sticky='nsew', padx=0, pady=0)
        
        guess_letter_rbutton = tk.Radiobutton(guess_choice_frame, text="Guess letter:", variable=self.selected_option, value="L: ", font=('Arial', 18))
        guess_letter_rbutton.grid(row=1, column=0, sticky='nsew', padx=0, pady=(10,5))
        self.current_input_letter = tk.Label(guess_choice_frame, text=f"", width=1)
        self.current_input_letter.grid(row=1, column=1, sticky='nsew')

        current_word_label = tk.Label(guess_choice_frame, text=f"Current entered word:")
        current_word_label.grid(row=2, column=1, sticky='nsew', padx=0, pady=0)

        guess_word_rbutton = tk.Radiobutton(guess_choice_frame, text="Guess word:", variable=self.selected_option, value="W: ", font=('Arial', 18))
        guess_word_rbutton.grid(row=3, column=0, sticky='nsew', padx=0, pady=(10,5))
        self.current_input_word = tk.Label(guess_choice_frame, text="", width=10)
        self.current_input_word.grid(row=3, column=1, sticky='nsew', padx=0, pady=0)

        bottom_right_frame.grid(row=1, column=2, sticky='nsew')

    def InitBottomFrame(self):
        # Bottom frame
        bottom_frame = ttk.Frame(self.game_frame)
        self.GenerateBottomLeftFrame(bottom_frame)
        self.GenerateBottomMiddleFrame(bottom_frame)
        self.GenerateBottomRightFrame(bottom_frame)

        bottom_frame.grid(row=1, column=0, sticky='nsew')
        
    def InitGameWindow(self):
        self.InitTopFrame()
        self.InitBottomFrame()
        

        
