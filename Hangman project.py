import random

# Predefined word list
WORDS = ["python", "hangman", "keyboard", "random", "variable"]

#ASCII art stages (0 wrong = safe, 6 wrong = hanged) 
HANGMAN_STAGES = [
    # 0 wrong
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    # 1 wrong
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    # 2 wrong
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    # 3 wrong
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    # 4 wrong
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    # 5 wrong
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    # 6 wrong – game over
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

MAX_WRONG = 6


def display_state(wrong_guesses, guessed_letters, secret_word):
    """Print the current gallows, masked word, and used letters."""
    print(HANGMAN_STAGES[wrong_guesses])
    print()

    # Show correctly guessed letters; hide the rest with 
    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f"  Word : {display}")
    print(f"  Wrong guesses left : {MAX_WRONG - wrong_guesses}")
    print(f"  Letters used       : {', '.join(sorted(guessed_letters)) or 'none'}")
    print()


def get_guess(guessed_letters):
    """Prompt the player for a single, unused letter."""
    while True:
        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  ⚠  Please enter a single letter (a–z).")
        elif guess in guessed_letters:
            print(f"  ⚠  You already guessed '{guess}'. Try another.")
        else:
            return guess


def play():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n" + "=" * 40)
    print("       W E L C O M E  T O  H A N G M A N")
    print("=" * 40)
    print(f"  The word has {len(secret_word)} letters. Good luck!\n")

    while wrong_guesses < MAX_WRONG:
        display_state(wrong_guesses, guessed_letters, secret_word)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"  🎉  You won! The word was: '{secret_word}'")
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"  ✔  '{guess}' is in the word!\n")
        else:
            wrong_guesses += 1
            remaining = MAX_WRONG - wrong_guesses
            print(f"  ✘  '{guess}' is NOT in the word. "
                  f"{remaining} guess{'es' if remaining != 1 else ''} left.\n")
    else:
        # Ran out of guesses
        display_state(wrong_guesses, guessed_letters, secret_word)
        print(f"  💀  Game over! The word was: '{secret_word}'")

    print("=" * 40 + "\n")


def main():
    while True:
        play()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing Hangman! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    main()
    