from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
correct_answer = random.randint(0, 100)
print(f"Pssst, the correct number is {correct_answer}")
while True:
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty in ['easy', 'hard']:
		break
	else:
		print("That is the incorrect input. Please try again.")

if difficulty == 'easy':
	guesses_remaining = 10
else:
	guesses_remaining = 5

print(f"You have {guesses_remaining} attempts remaining to guess the number.")

while guesses_remaining > 0:
	# Prompt the user to make a guess
	guess = int(input("Make a guess: "))

	# Check the validity of the guess
	if guess < correct_answer:
		print("Too low.")	
	elif guess > correct_answer:
		print("Too high.")
	else:
		print(f"You got it! The answer was {correct_answer}")
		# break
		guesses_remaining = 0
	
	guesses_remaining -= 1

	if guesses_remaining > 0:
		print("Guess again.")
		print(f"You have {guesses_remaining} remaining attempts to guess the number.")
	elif guesses_remaining == 0:
		print("You've run out of guesses, you lose.")

	
	
