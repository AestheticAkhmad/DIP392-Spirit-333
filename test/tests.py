import os
import sys
import unittest

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

import tkinter as tk
from GameMenu import GameMenu
from GamePage import GamePage

class WheelOfFortuneTest(unittest.TestCase):
    def setUp(self):
        self.main_window = tk.Tk()
        self.main_window.withdraw()
        self.main_window.geometry('1280x720')
        self.main_window.resizable(False, False)
        self.main_window.configure(bg='#E4D5B7')

        frame = tk.Frame(self.main_window, width=1280, height=720)
        frame.configure(bg='#E4D5B7')
        frame.grid(row=0, column=0)

        self.game_menu = GameMenu(self.main_window)

    def test_StartGameFail(self):
        self.game_menu.start_button.invoke()
        self.assertEqual(self.game_menu.info_label.cget("text"),
                         "Names must not be the same.\n"+
                         "Invalid name for Player 1.\nPlease use only numbers and English lettes.\n"+
                         "Invalid name for Player 2.\nPlease use only numbers and English lettes.")

    def test_StartGameSuccess(self):
        self.game_menu.player1_entry.insert(0, "Player123")
        self.game_menu.player2_entry.insert(0, "Player456")
        self.game_menu.start_button.invoke()

        self.assertEqual(self.game_menu.info_label.cget("text"),
                         "Please, use English letters and numbers.")
        
    def test_RotateWheelSuccess(self):
        self.game_menu.player1_entry.insert(0, "Player123")
        self.game_menu.player2_entry.insert(0, "Player456")
        self.game_menu.start_button.invoke()

        self.game_menu.game_page.rotate_button.invoke()
        self.assertFalse(self.game_menu.game_page.can_guess)

    def test_RotateWheelFail(self):
        self.game_menu.player1_entry.insert(0, "Player123")
        self.game_menu.player2_entry.insert(0, "Player456")
        self.game_menu.start_button.invoke()

        self.game_menu.game_page.rotate_button.invoke()
        self.assertFalse(self.game_menu.game_page.can_move)

    def tearDown(self) -> None:
        self.main_window.destroy()

if __name__ == "__main__":
    unittest.main()