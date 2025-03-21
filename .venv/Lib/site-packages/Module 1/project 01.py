import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Simple GUI Window")  # Set window title
root.geometry("400x300")  # Set window size (Width x Height)
root.resizable(False, False)  # Disable window resizing

def close_window():
    root.destroy()

# Create a close button
#close_button = tk.Button(root, text="Close", command= root.destroy)

close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack(pady=20)  # Add padding for better spacing

# Run the Tkinter event loop
root.mainloop()
