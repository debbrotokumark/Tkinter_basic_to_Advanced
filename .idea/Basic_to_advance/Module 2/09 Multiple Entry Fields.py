import tkinter as tk

root = tk.Tk()
root.title("Multiple Entries")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

root.mainloop()
