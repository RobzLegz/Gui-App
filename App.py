import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()  # holds the whole app

canvas = tk.Canvas(root, height=700, width=700,
                   bg="#263d42")  # styles the little window
canvas.pack()  # makes canvas attached to root

frame = tk.Frame(root, bg="#fff")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

root.mainloop()  # opens a little window
