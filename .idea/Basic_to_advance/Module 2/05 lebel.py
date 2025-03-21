import tkinter as tk

root = tk.Tk()
root.title("Label Example")
root.geometry("400x200")

# Create a label with some static text
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

def update_label():
    label1.config(text="Updated Text")



button = tk.Button(root, text="Update Text", command=update_label)
button.pack()

label1 = tk.Label(root, text="Static Text Example")
label1.pack()

#label = tk.Label(root, text="Custom Font Example", font=("Helvetica", 16, "bold"))
label = tk.Label(root, text="Custom Font Example", font=("Helvetica", 16, "bold italic"))

label.pack()

label = tk.Label(root, text="Custom Color Example", fg="red", bg="yellow")
label.pack()



"""
"n" (North) — Top center
"ne" (North East) — Top right corner
"e" (East) — Center-right
"se" (South East) — Bottom right corner
"s" (South) — Bottom center
"sw" (South West) — Bottom left corner
"w" (West) — Center-left
"nw" (North West) — Top left corner
"center" — Centered both horizontally and vertically
"""
label = tk.Label(root, text="Aligned Text Example", anchor="nw")
label.pack(fill=tk.BOTH, expand=True)


image = tk.PhotoImage(file="C:\\Users\\debkk\\PycharmProjects\\PyTkinter\\.venv\\Lib\\site-packages\\Module 1\\images\\icone.png")

# Create a label with the image
label = tk.Label(root, image=image)
label.pack()





root.mainloop()
