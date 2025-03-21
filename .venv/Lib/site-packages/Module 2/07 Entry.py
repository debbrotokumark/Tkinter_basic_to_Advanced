import tkinter as tk

root = tk.Tk()
root.title("Label Example")
root.geometry("400x200")

entry = tk.Entry(root,fg="red",bg="yellow")
entry.pack(pady=20)

entry = tk.Entry(root,fg="red",bg="yellow")
entry.insert(0,"Name")
entry.pack(pady=20)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

def on_entry_click(event):
    if name.get() == "Enter your text":
        name.delete(0, tk.END)
        name.config(fg="black")

def on_focus_out(event):
    if name.get() == "":
        name.insert(0, "Enter your text")
        name.config(fg="gray")

name = tk.Entry(root, fg="gray")
name.insert(0, "Enter your text")
name.bind("<FocusIn>", on_entry_click)
name.bind("<FocusOut>", on_focus_out)
name.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

def get_input():
    user_text = entry.get()
    print("User entered:", user_text)


# Button to fetch input
btn = tk.Button(root, text="Get Input", command=get_input)
btn.pack()

def clear_entry():
    entry.delete(0, tk.END)


entry = tk.Entry(root)
entry.pack(pady=10)

btn = tk.Button(root, text="Clear", command=clear_entry)
btn.pack()

entry = tk.Entry(root, text="Entry readonly", state="readonly")
entry.pack(pady=10)

# limit input
def validate_input(char, entry_value):
    return len(entry_value) < 10  # Limit input to 10 characters
vcmd = (root.register(validate_input), "%S", "%P")  # Tkinter validation

entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(pady=10)

#%S text being inserted or deleted (the change being made).
#%P Represents the proposed new value of the Entry widget if the change is allowed.


#Restricting Input to Numbers Only

def validate_number(char):
    return char.isdigit()  # Allow only digits
vcmd = (root.register(validate_number), "%S")

entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(pady=10)


root.mainloop()
