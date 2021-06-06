import random
w = open("words.txt").readlines()
a = random.choice(w)
guesses = 10
won = False
incorrect = []
correct = []
print("Hardest hangman ever! There are over 2000 words!")
print("You only have 6 guesses.")
print("Correct guesses are in random order")
input("Press enter to begin...")
print("Your word is " + str(len(a) - 1) + " characters long")
while guesses >0:
    if guesses < 11:
        guess = input("What is your guess? ")
        b = a.find(str(guess))
        if guess in a:
            print("Correct!")
            a = a.replace(guess, "")
            correct.append(guess)
            print("Correct guesses: " + str(correct))
            print("The word has " + str(len(a) - 1) + " characters left")
        else:
            print("Wrong!")
            guesses -= 1
            incorrect.append(guess)
            print("Incorrect guesses: " + str(incorrect))
            print("You have " + str(guesses) + " guesses remaining.")
        if len(a) == 1:
            won = True
            print("You win!")
            input("Press here to exit...")
        if won == True:
            break
if guesses == 0:
    print("You lose!")
    input("Press enter to exit...")
