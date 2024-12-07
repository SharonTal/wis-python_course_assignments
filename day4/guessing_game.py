import random

def main():
    print("Guessing Game!")
    while True:
        play_game()
        play_again = input("Do you want to play a new game? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break

def play_game():
    hidden_number = random.randint(1, 20)
    attempts = 0

    print("I have thought of a number between 1 and 20.")
    print("Type 'x' to exit the program, 'n' to start a new game, or 's' to reveal the hidden number.")
    
    while True:
        user_input = input("Take a guess: ").strip().lower()

        if user_input == 'x':
            print("Exiting the program. Goodbye!")
            exit()
        elif user_input == 'n':
            print("Starting a new game!")
            return
        elif user_input == 's':
            print(f"Cheating enabled! The hidden number is: {hidden_number}")
            continue

        if not user_input.isdigit():
            print("Invalid input. Please enter a number, 'x', 'n', or 's'.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < hidden_number:
            print("Your guess is too small!")
        elif guess > hidden_number:
            print("Your guess is too big!")
        else:
            print(f" You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
