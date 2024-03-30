import random

def choose_word():
    words = ["python", "hangman", "programming", "game", "algorithm","codealpha", "challenge", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def print_hangman(incorrect_guesses):
    hangman_figure = [
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "      |",
        "========="
    ]
    for line in hangman_figure[:incorrect_guesses]:
        print(line)

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print_hangman(incorrect_guesses)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print("Attempts left:", max_attempts - incorrect_guesses)
            if incorrect_guesses >= max_attempts:
                print("You lost! The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
