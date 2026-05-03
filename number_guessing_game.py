import random


def read_guess() -> int:
    while True:
        value = input("Enter your guess between 1 and 100: ").strip()

        if value.isdigit():
            guess = int(value)
            if 1 <= guess <= 100:
                return guess

        print("Please enter a valid number between 1 and 100.")


def play_game() -> None:
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nNumber Guessing Game")
    print("--------------------")

    while True:
        guess = read_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Correct. You guessed it in {attempts} attempts.")
            break


def main() -> None:
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()
