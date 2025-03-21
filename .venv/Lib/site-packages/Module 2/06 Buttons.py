import tkinter as tk

root = tk.Tk()
root.title("Debbroto")
root.geometry("500x300")  # Width=500, Height=300


window_width = 500
window_height = 300

btn = tk.Button(root, text="Click Me!")
btn.pack()

def on_button_click():
    btn.config(text="Button Clicked!")

btn = tk.Button(root, text="Click Me!", command=on_button_click)
btn.pack()

btn = tk.Button(
    root,
    text="Styled Button",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    width=15,
    height=2
)
btn.pack(pady=10)

btn = tk.Button(root, text="Padded", padx=100, pady=10)


btn.pack()

btn = tk.Button(root, text="Borderless", bd=10)
btn.pack()

btn = tk.Button(root, text="Disabled", state="disabled")
btn.pack()

canvas = tk.Canvas(root, width=200, height=100, bg="white", highlightthickness=0)
canvas.pack()

entry = tk.Entry(root)
entry.pack(pady=10)

# Run the application
root.mainloop()
