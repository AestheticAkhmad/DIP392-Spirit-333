import tkinter as tk
from tkinter import ttk
from List_of_words import word_hints
from Wheel import Wheel
import random
import collections

class GamePage:
    def __init__(self, main_window, menu_frame, player1, player2) -> None:
        self.main_window = main_window
        self.menu_frame = menu_frame
        self.game_frame = tk.Frame(main_window)
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
        self.can_guess = False
        self.current_bonus_label = None
        self.current_input_letter = None
        self.current_input_word = None
        self.word_start_idx = 0
        self.selected_option = "L"
        self.guessing_input_word = collections.deque()
        self.guessing_input_letter = ""
        self.one_player_left = False
        self.player_tries = 3

        self.InitGameWindow()
        self.ReadWordAndHint()
        main_window.bind("<Key>", self.GetPressedKey)
        self.game_frame.tkraise()

    def GetRandomNumber(self):
        return random.randint(0, 39)
    
    def GetRandomPlayerTurn(self):
        rand_num = random.randint(1, 2)
        if rand_num == 1:
            return 'P1'
        else:
            return 'P2'
    
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

    def ReadWordAndHint(self):
        random_number = self.GetRandomNumber()
        self.playing_word = list(word_hints[random_number].keys())[0].upper()
        self.hint = list(word_hints[random_number].values())[0]
        self.hint_label.config(text="Hint: "+ self.hint)

        self.to_guess_letters_count = len(self.playing_word)
        self.guessed_letters_count = 0

        self.word_letters = {char: False for char in self.playing_word}

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
    
    def ShowFoundLetters(self, indices):
        for i in indices:
            self.letter_tiles[i + self.word_start_idx].config(text=f"{self.playing_word[i]}")

    def ShowWholeWord(self):
        i = 0
        while i < len(self.playing_word):
            self.letter_tiles[i + self.word_start_idx].config(text=f"{self.playing_word[i]}")
            i += 1

    def UpdatePlayerScore(self):
        if self.player_turn == 'P1':
            self.player1.score += int(self.bonus)
            self.player1_score_label.config(text=f"{self.player1.name} Score: {self.player1.score}")
        else:
            self.player2.score += int(self.bonus)
            self.player2_score_label.config(text=f"{self.player2.name} Score: {self.player2.score}")

        self.can_move = True
    
    def GoToMenu(self):
        self.menu_frame.tkraise()

    def ExitGame(self):
        self.main_window.destroy()

    def InitGameOver(self):
        self.result_label.config(text=f'Both players lost the game!')

    def InitWinner(self, player):
        self.result_label.config(text=f'Winner:\n{player.name}!\nTotal score:{player.score}')

    def ChangePlayerTurn(self):
        if self.one_player_left:
            self.player_tries -= 1
            if self.player_tries <= 0:
                self.InitGameOver()
                return
        
        elif self.player_turn == 'P1':
            self.player_turn = 'P2'
        else:
            self.player_turn = 'P1'
        
        self.SetPlayerTurnLabel()
        self.can_move = True

    def GetPressedKey(self, event):
        current_letter = event.keysym
        if current_letter == "Return":
            if self.can_guess:
                if self.selected_option.get() == "LETTER":
                    if self.word_letters.get(self.guessing_input_letter, False):
                        return
                    
                    found, letters = self.FindLetter(self.guessing_input_letter)
                    if found == True:
                        self.word_letters[self.guessing_input_letter] = True
                        self.ShowFoundLetters(letters)
                        self.UpdatePlayerScore()

                        self.guessed_letters_count += len(letters)

                        if self.guessed_letters_count == self.to_guess_letters_count:
                            if self.player_turn == 'P1':
                                self.InitWinner(self.player1)
                                return
                            else:
                                self.InitWinner(self.player2)
                                return

                    else:
                        self.ChangePlayerTurn()

                elif self.selected_option.get() == "WORD":
                    guess_word_str = ''.join(self.guessing_input_word)

                    if guess_word_str == self.playing_word:
                        self.ShowWholeWord()
                        self.UpdatePlayerScore()
                        if self.player_turn == 'P1':
                            self.InitWinner(self.player1)
                            return
                        else:
                            self.InitWinner(self.player2)
                            return
                    else:
                        self.ChangePlayerTurn()
                        self.one_player_left = True
                
                self.can_guess = False
                

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

    def InitPlayerBankrupcy(self):
        if self.player_turn == 'P1':
            self.player1.score = 0
            self.player1_score_label.config(text=f"{self.player1.name} Score: {self.player1.score}")
        else:
            self.player2.score = 0
            self.player2_score_label.config(text=f"{self.player2.name} Score: {self.player2.score}")

        if not self.one_player_left:
            self.ChangePlayerTurn()
        else:
            self.player_tries -= 1

        if self.player_tries <= 0:
            self.InitGameOver()
            return

        self.can_move = True

    def StartWheelRotation(self):
        print(self.selected_option.get())
        if self.can_move == True:
            self.can_move = False
            self.current_bonus_label.config(text=f'Rotating...')
            def SetBonusLabel(angle):
                self.bonus = self.wheel.GetBonus(angle)
                if self.bonus != 'Backruptcy':
                    self.current_bonus_label.config(text=f'${self.bonus}')
                    self.can_guess = True
                else:
                    self.current_bonus_label.config(text=f'{self.bonus}')
                    self.InitPlayerBankrupcy()
                    self.SetPlayerTurnLabel()
                    self.can_guess = False
                    self.can_move = True

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
        home_button = tk.Button(top_frame, text="Home", command=lambda: self.GoToMenu())
        home_button.grid(row=0, column=1, sticky='nse', padx=10, pady=(20, 10))
        home_button.config(height=2, width=10)

        exit_button = tk.Button(top_frame, text="Exit", command=lambda: self.ExitGame())
        exit_button.grid(row=0, column=2, sticky='nse', padx=10, pady=(20, 10))
        exit_button.config(height=2, width=10)
        
        top_frame.grid(row=0, column=0, sticky='nsew', pady=(30, 30))

    def GenerateBottomLeftFrame(self, bottom_frame):
        # Hint label
        bottom_left_frame = tk.Frame(bottom_frame, width=400)
        self.hint_label = tk.Label(bottom_left_frame, text="", font=('Arial', 26))
        self.hint_label.grid(row=0, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

        self.rule_label = tk.Label(bottom_left_frame, text="Rule: press alphabetic letter and Enter key.", font=('Arial', 16))
        self.rule_label.grid(row=1, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

        self.result_label = tk.Label(bottom_left_frame, text="", font=('Helvetica', 32, 'bold'))
        self.result_label.grid(row=2, column=0, sticky='nsw', padx=(10, 5), pady=(5, 5))

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

    def SetPlayerTurnLabel(self):
        if self.player_turn == 'P1':
            self.turn_label.config(text=f'{self.player1.name}\'s turn.')
        elif self.player_turn == 'P2':
            self.turn_label.config(text=f'{self.player2.name}\'s turn.')

    def GenerateBottomRightFrame(self, bottom_frame):
        # Bottom right frame
        bottom_right_frame = ttk.Frame(bottom_frame)

        # Player scores labels
        self.player1_score_label = tk.Label(bottom_right_frame, text=f"{self.player1.name} Score: 0")
        self.player1_score_label.grid(row=0, column=0, sticky='nsew', padx=0, pady=0)

        self.player2_score_label = tk.Label(bottom_right_frame, text=f"{self.player2.name} Score: 0")
        self.player2_score_label.grid(row=1, column=0, sticky='nsew', padx=0, pady=0)

        # Player's turn label
        self.turn_label = tk.Label(bottom_right_frame, text=f"NONE Turn", bg='blue', fg='white')
        self.turn_label.grid(row=2, column=0, sticky='nsew', padx=0, pady=0)
        self.SetPlayerTurnLabel()

        # Guess placements
        self.selected_option = tk.StringVar()

        guess_choice_frame = ttk.Frame(bottom_right_frame)
        guess_choice_frame.grid(row=3, column=0, sticky='nsew', padx=0, pady=(10, 10))

        current_letter_label = tk.Label(guess_choice_frame, text=f"Current entered letter:")
        current_letter_label.grid(row=0, column=1, sticky='nsew', padx=0, pady=0)
        
        guess_letter_rbutton = tk.Radiobutton(guess_choice_frame, text="Guess letter:", variable=self.selected_option, value="LETTER", font=('Arial', 18))
        guess_letter_rbutton.grid(row=1, column=0, sticky='nsew', padx=0, pady=(10,5))
        self.current_input_letter = tk.Label(guess_choice_frame, text=f"", width=1)
        self.current_input_letter.grid(row=1, column=1, sticky='nsew')

        current_word_label = tk.Label(guess_choice_frame, text=f"Current entered word:")
        current_word_label.grid(row=2, column=1, sticky='nsew', padx=0, pady=0)

        guess_word_rbutton = tk.Radiobutton(guess_choice_frame, text="Guess word:", variable=self.selected_option, value="WORD", font=('Arial', 18))
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
        

        
