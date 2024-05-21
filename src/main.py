import tkinter as tk
from GameMenu import GameMenu

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.geometry('1280x720')
    main_window.resizable(False, False)
    main_window.configure(bg='#E4D5B7')

    frame = tk.Frame(main_window, width=1280, height=720)
    frame.configure(bg='#E4D5B7')
    frame.grid(row=0, column=0)

    game_menu = GameMenu(main_window)

    main_window.mainloop()