from tkinter import PhotoImage

import tkinter as tk

# Create main window
root = tk.Tk()


root.title("Debbroto")
root.geometry("500x300")  # Width=500, Height=300
#root.geometry("500x300+400+200")  # 500x300 window, placed at (400,200)


window_width = 500
window_height = 300


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

#root.geometry(f"{window_width}x{window_height}+{x}+{y}")


root.resizable(False, False)  # Disables window resizing


# Run the application
root.mainloop()
