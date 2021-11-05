#1.  Make a program that selects a word from a list of words
# 2. From each category, select a random word
# 3. Accept user input that asks the user to type in a category
# randomly_selected_word = "orange"
# 4. _ _ _ _ _ _
# 5. if you make a correct choice = "o" => o _ _ _ _ _
# randomly_selected_word = "watermelon"
# 6. _ _ _ _ _ _ _ _ _ _ _
# 7. if you make a correct choice = "e" => _ _ _ e _ _ e _ _ _
# 8. 7 attempts
# 9. if you exhausted all 7 choices, show the correct word

#setting up varialbes
import random
guess_words = ["pineapple","pear","orange","banana","mango","apple","grape","watermelon", "peach", "dragonfruit"]

answer = random.choice(guess_words)
incorrect_guess_total = 0
guessed_letters = []
incorrect_letters = []

#Running the game
print("Welcome to hangman!")

game_over = False
while game_over == False:
    guess = input("What is your next Guess?")
    guessed_letters.append(guess)

    done = False
    while not done:
        for letter in answer:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        if guess not in answer:
            incorrect_guess_total += 1
            incorrect_letters.append(guess)
        done = True


    print("totally incorrect guesses:" + str(incorrect_guess_total))
    print("incorrect letters:" + str(incorrect_letters))
    if incorrect_guess_total == 7:
        print("Game over!")
        game_over == True


