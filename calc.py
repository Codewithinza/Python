import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Python Calculator")
window.geometry("300x400")  # Set the window size (width x height)
window.configure(bg="#301934")  # Set the background color of the window
window.resizable(True, True)  # Disable window resizing

# Create a frame for the display and buttons
frame = tk.Frame(window, bg="#301934")
frame.pack(pady=10)

# Create the display
display = tk.Entry(frame, width=20, font=("Arial", 20), justify=tk.RIGHT, bg="#D8BFD8", fg="#ffffff")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0
for button in buttons:
    if button == "=":
        btn = ttk.Button(frame, text=button, width=5, style="EqualButton.TButton", command=button_equal)
    else:
        btn = ttk.Button(frame, text=button, width=5, style="NumberButton.TButton", command=lambda num=button: button_click(num))

    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button
clear_btn = ttk.Button(frame, text="C", width=5, style="ClearButton.TButton", command=button_clear)
clear_btn.grid(row=row, column=col, padx=5, pady=5)

# Configure the styles for the buttons
style = ttk.Style()
style.configure("NumberButton.TButton", background="#616161", foreground="#ffffff", font=("Arial", 14))
style.configure("EqualButton.TButton", background="#ff6f00", foreground="#ffffff", font=("Arial", 14))
style.configure("ClearButton.TButton", background="#b71c1c", foreground="#ffffff", font=("Arial", 14 ,))

# Configure the grid to expand with the window
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

# Run the main loop
window.mainloop()
