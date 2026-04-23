# # guess a number between a range of numbers
import random

print('NUMBER GUESSING GAME...')

start = int(input('enter starting number: '))
end = int(input('enter ending number: '))
num = random.randint(start, end)

chance = 7 # total chances
count = 0 # counter for the guess

while count < chance:
    count += 1
    guess = int(input("enter your guess: "))

    if guess == num:
        print("congrats! correct guess...")
    elif count >= chance and guess != num:
        print('better luck next time...')
    elif guess > num:
        print('guess is too high')
    elif guess < num:
        print('guess is too low')

        