import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()  # holds the whole app

canvas = tk.Canvas(root, height=700, width=700, bg="#263d42")
canvas.pack()

root.mainloop()  # opens a little window
