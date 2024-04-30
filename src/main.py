import tkinter as tk
from tkinter import ttk
from GameMenu import GameMenu
from GamePage import GamePage
from PIL import Image, ImageTk

main_window = tk.Tk()
main_window.geometry('1280x720')
main_window.resizable(False, False)

# style = ttk.Style()
# style.configure("My.TFrame", background='blue')
# frame = ttk.Frame(main_window, style="My.TFrame", width=1280, height=720)
# frame.pack()

game_menu = GameMenu(main_window)

main_window.mainloop()



# background_image = Image.open("/Users/akhmadoripov/Proj/wheel_of_fortune/DIP392-Spirit-333/src/turtle.jpg")
# photo = ImageTk.PhotoImage(background_image.resize((1280, 720)))

# canvas = tk.Canvas(main_window)
# canvas.pack(fill='both', expand=True)
# canvas.create_image(0, 0, anchor='nw', image=photo)

# # background_label = tk.Label(main_window, image=background_image)
# # background_label.place(x=0, y=0, relwidth=1, relheight=1)