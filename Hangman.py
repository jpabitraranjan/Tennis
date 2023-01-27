# player1
word = input('Word:').lower()
hint = input("Enter the hint: ")
# game setup
lives = 6
guesses = ''
# gap
for i in range(100):
    print('*')
# info for player2
print("HANGMAN\nYou have 6 lives.")
print('HINT:', hint)
# game
while lives > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won!")
        break
    guess = input("Guess a letter:").lower()
    guesses += guess
    if guess not in word:
        lives -= 1
        print("Wrong! You have " + str(lives) + " lives left.")
    if lives == 0:
        print("You lost!")
