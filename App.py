import tkinter as tk
from tkinter import Label, filedialog, Text
import os

root = tk.Tk()  # holds the whole app
apps = []


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*exe"), ("all files", "*.*")))  # shows all .exe files
    apps.append(filename)
    for app in apps:

        # adds a label with a location of your app
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()


canvas = tk.Canvas(root, height=700, width=700,
                   bg="#263d42")  # styles the little window
canvas.pack()  # makes canvas attached to root

frame = tk.Frame(root, bg="#fff")  # adds a little box in the popup
frame.place(relwidth=0.8, relheight=0.8, relx=0.1,
            rely=0.1)  # sizes of the box
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="#fff", bg="#263d42", command=addApp)
openFile.pack()
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="#fff", bg="#263d42")
runApps.pack()

root.mainloop()  # opens a little window
