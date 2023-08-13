import random
import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("Hangman Game")
    new_window.geometry("400x300")
    new_window.configure(bg="#E6C7C7")  # Set background color to a pastel shade

    words = ['apple', 'banana', 'orange', 'cherry', 'watermelon', 'grape', 'pineapple']
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    def guess_letter():
        nonlocal tries
        guess = letter_entry.get().lower()
        letter_entry.delete(0, tk.END)

        if len(guess) != 1:
            result_label.config(text="Please enter a single letter.")
            return

        if guess in guessed_letters:
            result_label.config(text="You've already guessed that letter.")
            return

        if guess not in word:
            tries -= 1

        guessed_letters.append(guess)
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        guessed_word_label.config(text=guessed_word)
        tries_label.config(text=f"Tries left: {tries}")

        if "_" not in guessed_word:
            result_label.config(text="Congratulations! You guessed the word.")
            submit_button.config(state=tk.DISABLED)

        if tries == 0:
            result_label.config(text=f"You ran out of tries. The word was: {word}")
            submit_button.config(state=tk.DISABLED)

    guessed_word_label = tk.Label(new_window, text="_" * len(word), font=("Arial", 24), bg="#E6C7C7")
    guessed_word_label.pack(pady=20)

    letter_entry = tk.Entry(new_window, font=("Arial", 14))
    letter_entry.pack()

    submit_button = tk.Button(new_window, text="Submit", command=guess_letter)
    submit_button.pack(pady=10)

    tries_label = tk.Label(new_window, text=f"Tries left: {tries}", font=("Arial", 14), bg="#E6C7C7")
    tries_label.pack()

    result_label = tk.Label(new_window, text="", font=("Arial", 14), bg="#E6C7C7")
    result_label.pack(pady=10)

root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")
root.configure(bg="#E6C7C7")  # Set background color to a pastel shade

start_button = tk.Button(root, text="Start Game", command=open_new_window)
start_button.pack(pady=50)

root.mainloop()
