correct_number = 30
while True:
    guess = int(input("Guess the number: "))

    if guess == correct_number:
        print("Congratulations, you guessed correctly!")
        break
    else:
        print("Incorrect guess. Try again.")
