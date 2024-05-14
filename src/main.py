import tkinter as tk
from tkinter import ttk
from GameMenu import GameMenu
from GamePage import GamePage
from PIL import Image, ImageTk

main_window = tk.Tk()
main_window.geometry('1280x720')
main_window.resizable(False, False)

game_menu = GameMenu(main_window)

main_window.mainloop()