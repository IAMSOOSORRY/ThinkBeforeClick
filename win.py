import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Phishing Awareness Game - You won")

# Load the image
image = Image.open("win.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=photo)
label.pack()

# Make the window fullscreen
root.attributes('-fullscreen', True)

# Allow exiting fullscreen with the 'Escape' key
root.bind('<Escape>', lambda e: root.attributes('-fullscreen', False))

# Start the main event loop
root.mainloop()
