import tkinter as tk
from tkinter import Label, filedialog, Text
import os

root = tk.Tk()  # holds the whole app
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]


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


def runApps():
    for app in apps:
        os.startfile(app)  # opens all selected apps


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
                    pady=5, fg="#fff", bg="#263d42", command=runApps)
runApps.pack()
clearFiles = tk.Button(root, text="Close All", padx=10,
                       pady=5, fg="#fff", bg="#263d42")
clearFiles.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()  # opens a little window

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
