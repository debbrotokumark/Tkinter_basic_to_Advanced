import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you really want to exit?"):
        root.destroy()  # Close the window

root = tk.Tk()
root.title("WM_DELETE_WINDOW Example")

# Handle the window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
