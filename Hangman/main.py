import random

import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

lives = 6

print(hangman_art.logo)

# Création des underscores ['_']
display = []
for chosen_letter in range(len(chosen_word)):
    display += "_"
print(display)

while "_" in display:
    print(f"{lives} left")
    user_guess = input("Guess a letter: ").lower()

    if user_guess in display:
        print("This letter has been already used")

    # Vérification de la lettre devinée par l'utilisateur
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter.replace("_", user_guess)

    if user_guess not in chosen_word:
        lives -= 1
        print(user_guess + " is not a correct letter")

    if lives == 0:
        print("You Lose")
        exit() # Permet d'arrêter l'exécution de la condition while

    if "_" not in display:
        print("You Won!")

    print(hangman_art.stages[lives])
    print(display)
