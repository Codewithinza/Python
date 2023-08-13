import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("Web Scraper Results")
    new_window.geometry("800x600")
    new_window.configure(bg="#E6C7C7")  # Set background color to a pastel shade

    url = url_entry.get()

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract information from the webpage
        title = soup.title.string.strip()
        body_text = soup.get_text().strip()

        # Create a Text widget to display the extracted information
        text_widget = tk.Text(new_window, font=("Arial", 12))
        text_widget.pack()

        # Insert the extracted information into the Text widget
        text_widget.insert(tk.END, f"Title: {title}\n\nBody Text:\n{body_text}")

        # Make the Text widget read-only
        text_widget.configure(state=tk.DISABLED)

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred:\n\n{e}")

root = tk.Tk()
root.title("Web Scraper")
root.geometry("400x300")
root.configure(bg="#E6C7C7")  # Set background color to a pastel shade

url_label = tk.Label(root, text="Enter URL:", font=("Arial", 12), bg="#E6C7C7")
url_label.pack()

url_entry = tk.Entry(root, font=("Arial", 12))
url_entry.pack()

start_button = tk.Button(root, text="Start Web Scraper", command=open_new_window)
start_button.pack(pady=20)

root.mainloop()
