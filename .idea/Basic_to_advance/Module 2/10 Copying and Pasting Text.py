import tkinter as tk

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(entry.get())
    root.update()

def paste_text():
    entry.insert(tk.END, root.clipboard_get())

root = tk.Tk()
root.title("Copy & Paste in Entry")

entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Copy", command=copy_text).pack()
tk.Button(root, text="Paste", command=paste_text).pack()

root.mainloop()
