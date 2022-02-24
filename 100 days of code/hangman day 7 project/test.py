import random, os
from hangman_ascii import hangman, logo
from wordlist import word_list

#ascii arts

# hangman = hangman_ascii.hangman
# word_list = wordlist.word_list
# logo = hangman_ascii.h_text



glob_cnt = 0
lives = 6

## functions
def clear():
    os.system('cls')

def proceed():
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    

def take_life():
    global glob_cnt
    
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(hangman[glob_cnt])
    glob_cnt += 1


chosen_word = random.choice(word_list)
display = []
for _ in chosen_word:
    display += "_"


print(logo)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()
    clear()
    
    if guess in chosen_word:
        proceed()
    else:
        lives -= 1
        take_life()
        if lives == 0:
            end_of_game = True
            print("Game Over!")
    print(f"{''.join(display)}")

    if "_" not in display:
        print("You Won!")
        end_of_game = True