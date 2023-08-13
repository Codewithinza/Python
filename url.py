import tkinter as tk
import webbrowser
import random


# Function to generate a random pastel color
def generate_pastel_color():
    r = random.randint(64, 192)
    g = random.randint(64, 192)
    b = random.randint(64, 192)
    return "#%02x%02x%02x" % (r, g, b)


# Function to shorten the URL and open it in a new window
def shorten_url():
    # Get the URL from the user input
    url = entry.get()

    # Open the shortened URL in a new browser window
    webbrowser.open_new(url)


# Create the GUI window
window = tk.Tk()
window.title("URL Shortener")
window.geometry("300x150")

# Create a label, entry, and button widgets
label = tk.Label(window, text="Enter the URL:", pady=10)
label.pack()

entry = tk.Entry(window, width=30)
entry.pack()

button = tk.Button(window, text="Shorten URL", bg=generate_pastel_color(), command=shorten_url)
button.pack()

# Run the GUI event loop
window.mainloop()
