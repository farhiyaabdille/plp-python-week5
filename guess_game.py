secret_number = 13
attempts = 0

print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Congratulations! You guessed it!")
        break

print(f"You got it in {attempts} tries!")
