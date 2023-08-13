import random
import tkinter as tk
from tkinter import messagebox
from random import choice

# List of pastel colors
pastel_colors = ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BFFFBF', '#BAE1FF', '#D7BAFF']

class GuessGame:
    def __init__(self):
        self.target_number = random.randint(1, 10)
        self.attempts = 0

        self.root = tk.Tk()
        self.root.title("Pastel Guess Game")
        self.root.geometry("300x150")
        self.root.configure(bg=choice(pastel_colors))

        self.title_label = tk.Label(self.root, text="Welcome to the Pastel Guess Game!", font=("Arial", 12), bg=self.root.cget("bg"))
        self.title_label.pack(pady=10)

        self.guess_label = tk.Label(self.root, text="Enter your guess (between 1 and 10):", font=("Arial", 10), bg=self.root.cget("bg"))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.root, font=("Arial", 10), width=10)
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self.root, text="Guess", font=("Arial", 10), command=self.check_guess)
        self.guess_button.pack()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess == self.target_number:
                messagebox.showinfo("Congratulations!", "You guessed the number!")
                self.root.destroy()
            elif guess < self.target_number:
                messagebox.showinfo("Too Low", "Too low. Try again.")
            else:
                messagebox.showinfo("Too High", "Too high. Try again.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

game = GuessGame()
game.root.mainloop()
