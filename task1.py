import random

words = ["SMARTPHONE", "CAT", "TELEVISION", "LAPTOP"]
word = random.choice(words)

total_chances = 7
guess_word = "-" * len(word)

while total_chances != 0:
    print(guess_word)
    letter = input("Guess a letter: ").upper()
    
    if letter in word:
        new_guess_word = list(guess_word)
        for i in range(len(word)):
            if word[i] == letter:
                new_guess_word[i] = letter
        guess_word = "".join(new_guess_word)
        print(guess_word)
        
        if guess_word == word:
            print("Congratulations! You won!!")
            break
        
    else:
        total_chances -= 1
        print("Incorrect guess")
        print("The remaining chances are", total_chances)

else:
    print("Game Over")
    print("You Lose")
    print("All the chances are exhausted")
    print("The correct word was", word)
