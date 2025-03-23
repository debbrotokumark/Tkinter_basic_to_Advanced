import tkinter as tk


root = tk.Tk()
root.title("Multi-line Text Input")

text_widget = tk.Text(root, height=5, width=40)
text_widget.pack()


text_widget = tk.Text(root, height=10, width=40)
text_widget.pack(padx=10, pady=10)

# Insert text at specific positions in the Text widget
# Insert at the very beginning of the text (line 1, column 0)
text_widget.insert("1.0", "This is the first line.\n")

# Insert at the start of the second line (line 2, column 0)
text_widget.insert("2.0", "This is the second line.\n")

# Insert at the 5th character of the second line (line 2, column 4)
text_widget.insert("2.3", "INSERTED ")

# Insert at the end of the text
text_widget.insert("end", "\nThis is the last line.")


text_widget = tk.Text(root, height=10, width=40)
text_widget.pack(padx=10, pady=10)


text_widget.insert("1.0", "This is the first line.\n")
text_widget.delete("1.0", "end") # Delete all text
text_widget.pack()

text_widget.insert("1.0", "This is a formatted text.")

# Add a tag
text_widget.tag_add("bold", "1.0", "1.4")  # Bold the first word
text_widget.tag_config("bold", font=("Arial", 12, "bold"))
text_widget.pack()


# image = tk.PhotoImage(file="C:\\Users\\debkk\\PycharmProjects\\PyTkinter\\.idea\\Basic_to_advance\\Module 1\\images\\icone.png",height=100,width=60)
# text_widget.image_create("end", image=image)
# text_widget.pack()
#

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")
text_widget = tk.Text(root)

text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)


root.mainloop()
