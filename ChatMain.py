import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def check_pin():
    user_input = pin_entry.get()
    if user_input == '0945':
        root.destroy()
        os.system("python ChatWindow.py")
    else:
        messagebox.showinfo("Incorrect Pin", "Please enter the correct pin.", icon="warning")

root = tk.Tk()
root.title("Messenger")

# Set a fixed window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Load and display the image
image = Image.open("Chat/ChatPin.png")
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.pack()

# Entry for PIN input
pin_entry = tk.Entry(root, font=('Courier New', 28), foreground="black", width=18, show="*")
pin_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=check_pin, font=("Helvetica", 20, "bold"))
submit_button.pack()

root.mainloop()
