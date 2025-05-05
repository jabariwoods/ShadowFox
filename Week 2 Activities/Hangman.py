import random
import string
import os # Optional: for clearing the screen for a cleaner look

# --- Word List ---
WORDS = [
    "PYTHON", "JAVASCRIPT", "DEVELOPER", "HANGMAN", "PROGRAMMING",
    "COMPUTER", "SCIENCE", "ALGORITHM", "DATABASE", "INTERFACE",
    "NETWORK", "FRAMEWORK", "DEBUGGING", "VARIABLE", "FUNCTION"
]

# --- Hangman Visuals ---
# Stages of the hangman based on incorrect guesses
HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# --- Helper Functions ---

def clear_screen():
  """Clears the console screen (works on Windows, Linux, macOS)."""
  os.system('cls' if os.name == 'nt' else 'clear')

def get_random_word(word_list):
  """Selects a random word from the provided list."""
  word = random.choice(word_list)
  return word.upper() # Ensure word is uppercase for consistency

def display_game_state(hangman_pics, incorrect_guesses_count, guessed_letters, secret_word):
  """Displays the current hangman visual, guessed letters, and word progress."""
  print(hangman_pics[incorrect_guesses_count])
  print()

  # Show incorrect letters
  incorrect_letters_str = " ".join(sorted([letter for letter in guessed_letters if letter not in secret_word]))
  if incorrect_letters_str:
      print(f"Incorrect guesses: {incorrect_letters_str}")
  else:
      print("Incorrect guesses: None yet")

  # Show the word with underscores for unguessed letters (hints)
  word_progress = ""
  for letter in secret_word:
    if letter in guessed_letters:
      word_progress += letter + " "
    else:
      word_progress += "_ "
  print(f"Word: {word_progress}")
  print("-" * 30) # Separator

def get_guess(guessed_letters):
    """Prompts the player for a letter guess and validates it."""
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter only a single letter.")
        elif guess not in string.ascii_uppercase:
            print("Please enter a LETTER.")
        elif guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try again.")
        else:
            return guess

# --- Main Game Logic ---

def play_game():
  """Runs a single round of the Hangman game."""
  secret_word = get_random_word(WORDS)
  word_letters = set(secret_word) # Set of unique letters in the word
  guessed_letters = set()         # Set of letters the user has guessed
  incorrect_guesses_count = 0
  max_attempts = len(HANGMAN_PICS) - 1 # Usually 6 incorrect guesses allowed

  print("Welcome to Hangman!")

  while True:
    clear_screen() # Optional: Clear screen each turn
    display_game_state(HANGMAN_PICS, incorrect_guesses_count, guessed_letters, secret_word)

    # --- Check Win/Loss Conditions BEFORE getting next guess ---
    # Win Condition: All letters in the word have been guessed
    if word_letters.issubset(guessed_letters): # or len(word_letters) == 0 if removing letters
        print(f"Congratulations! You guessed the word: {secret_word}")
        break # Exit the game loop (player won)

    # Loss Condition: Reached max incorrect attempts
    if incorrect_guesses_count >= max_attempts:
        print("Sorry, you ran out of attempts!")
        print(f"The word was: {secret_word}")
        print(HANGMAN_PICS[max_attempts]) # Show the final hangman
        break # Exit the game loop (player lost)

    # --- Get User Input ---
    guess = get_guess(guessed_letters)
    guessed_letters.add(guess) # Add the valid guess to the set

    # --- Check Guess ---
    if guess in word_letters:
        print(f"Good guess! '{guess}' is in the word.")
        # Optional: Remove the letter if tracking remaining letters this way
        # word_letters.remove(guess)
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses_count += 1

    input("Press Enter to continue...") # Pause briefly

# --- Play Again Loop ---

def main():
  """Main function to handle playing multiple games."""
  while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes' and play_again != 'y':
      print("Thanks for playing Hangman!")
      break

# --- Start the game ---
if __name__ == "__main__":
  main()
