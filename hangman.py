import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_words = []
end_of_game = False
lives = 6

print(logo)

display = ["_"] * word_length
print(display)  

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_words:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        continue
    
    guessed_words.append(guess)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You have died! The word was {chosen_word}")
            break

    if not end_of_game:
        print(f"{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("You have won!")

    print(stages[lives])
