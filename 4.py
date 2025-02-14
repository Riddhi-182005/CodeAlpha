import random
import nltk
from nltk.corpus import words

# Download word list (only needed once)
nltk.download('words')

# Get a list of English words
word_list = words.words()

# Select a random word (ensure it's a reasonable length)
word = random.choice([w.lower() for w in word_list if len(w) > 4 and len(w) < 10])
hidden_word = ["_"] * len(word)
attempts = 6  # Maximum incorrect guesses

print("🎯 Welcome to Hangman! Guess the word.")

while attempts > 0 and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    if "_" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

if "_" in hidden_word:
    print("\n💀 Game over! The word was:", word)
