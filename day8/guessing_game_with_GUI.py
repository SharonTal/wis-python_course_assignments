import random
import tkinter as tk
from tkinter import messagebox

def start_new_game():
    global hidden_number, attempts
    hidden_number = random.randint(1, 20)
    attempts = 0
    guess_entry.delete(0, tk.END)
    status_label.config(text="I have thought of a number between 1 and 20.")

def check_guess():
    global attempts
    user_input = guess_entry.get().strip().lower()

    if user_input == '':
        messagebox.showinfo("Invalid Input", "Please enter a number, 'x', 'n', or 's'.")
        return

    if user_input == 'x':
        root.destroy()
        return
    elif user_input == 'n':
        start_new_game()
        return
    elif user_input == 's':
        messagebox.showinfo("Reveal Number", f"The hidden number is: {hidden_number}")
        return

    if not user_input.isdigit():
        messagebox.showinfo("Invalid Input", "Please enter a valid number.")
        return

    guess = int(user_input)
    attempts += 1

    if guess < hidden_number:
        status_label.config(text="Your guess is too small!")
    elif guess > hidden_number:
        status_label.config(text="Your guess is too big!")
    else:
        messagebox.showinfo("Congratulations!", f"You guessed the number in {attempts} attempts.")
        start_new_game()

# Initialize main game window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f8ff")  # Light blue background

# Game Variables
hidden_number = random.randint(1, 20)
attempts = 0

# Widgets
header_label = tk.Label(root, text="Welcome to the Guessing Game!", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082")
header_label.pack(pady=10)

status_label = tk.Label(root, text="I have thought of a number between 1 and 20.", font=("Helvetica", 12), bg="#f0f8ff", fg="#4b0082")
status_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Helvetica", 14), justify="center", width=10)
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", font=("Helvetica", 12), command=check_guess, bg="#4b0082", fg="white")
guess_button.pack(pady=10)

new_game_button = tk.Button(root, text="Start New Game", font=("Helvetica", 12), command=start_new_game, bg="#32cd32", fg="white")
new_game_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=root.destroy, bg="#ff4500", fg="white")
exit_button.pack(pady=5)

# Start the main loop
root.mainloop()
