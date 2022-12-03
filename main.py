import random
from art import stages, logo
from word_list import word_list
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed the letter {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"Letter {guess} is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lost")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
