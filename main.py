import random, os
from hangman_art import stages, logo
from hangman_words import word_list
from sys import platform

clear = lambda: os.system("clear")
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
game_ended = False
clear()
print(logo)

display = []
for _ in range(word_length):
    display.append("_")

while not game_ended:
    guess = (input("Guess a letter: ")).lower()
    clear()
    if guess in display:
        print(f"You've already tried {guess}. Try a different letter.")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose 1 life.")
        lives -= 1
        if lives == 0:
            game_ended = True
            print("You lost.")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        game_ended = True
        print("You won!")
    
    print(stages[lives])
     
    
        

     