import tkinter as tk
from tkinter import ttk

class GamePage:
    def __init__(self, main_window) -> None:
        self.game_frame = ttk.Frame()
        self.game_frame.grid(row=0, column=0, sticky='nsew')
        self.letter_tiles = list()
        self.hint_label = None

        self.open_game_window()
        self.game_frame.tkraise()

    def ReadWordAndHint():
        pass

    def open_game_window(self):
        # Top Frame
        top_frame = ttk.Frame(self.game_frame)

        # Creating 12 tiles for letters
        tiles_frame = ttk.Frame(top_frame)
        tiles_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=(20, 10))
        for i in range(12):
            tile_label = ttk.Label(tiles_frame, text=" A ", font=('Arial', 40), borderwidth=1, relief="raised")
            tile_label.pack(side="left", padx=2)
            self.letter_tiles.append(tile_label)


        # Home button
        home_button = tk.Button(top_frame, text="Home")
        home_button.grid(row=0, column=1, sticky='nsew', padx=10, pady=(20, 10))
        home_button.config(height=2, width=10)

        exit_button = tk.Button(top_frame, text="Exit")
        exit_button.grid(row=0, column=2, sticky='nsew', padx=10, pady=(20, 10))
        exit_button.config(height=2, width=10)

        # Bottom frame
        bottom_frame = ttk.Frame(self.game_frame)

        # Hint label
        self.hint_label = tk.Label(bottom_frame, text="Hint: ")
        self.hint_label.grid(row=0, column=0, sticky='nsew', padx=(10, 5), pady=(5, 5))

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
        bottom_middle_frame.grid(row=1, column=1, sticky='nsew')
        bottom_right_frame.grid(row=1, column=2, sticky='nsew')

        
