from art import logo
import random

def main():
	correct_answer = start()
	difficulty = validate_input()
	guesses_remaining = level_of_play(difficulty)
	
	print(f"You have {guesses_remaining} attempts remaining to guess the number.")

	while guesses_remaining > 0:
		# Prompt the user to make a guess
		guess = int(input("Make a guess: "))

		# Check the validity of the guess
		guesses_remaining = check_answer(x = guess, y = correct_answer, z = guesses_remaining)
		
		if guesses_remaining > 0:
			print("Guess again.")
			print(f"You have {guesses_remaining} remaining attempts to guess the number.")
		elif guesses_remaining == 0:
			print("You've run out of guesses, you lose.")


def check_answer(x, y, z):
	if x < y:
		print("Too low.")	
	elif x > y:
		print("Too high.")
	else:
		print(f"You got it! The answer was {y}")
		# break
		return -1
	z -= 1
	return z

def validate_input():
	while True:
		answer = input("Choose a difficulty. Type 'easy' or 'hard': ")
		if answer in ['easy', 'hard']:
			break
		else:
			print("That is the incorrect input. Please try again.")
	return answer


def level_of_play(x):
	if x == 'easy':
		return 10
	else:
		return 5	

def start():
	print(logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	x = random.randint(0, 100)
	print(f"Pssst, the correct number is {x}")
	return x

if __name__ == '__main__':
	main()


	
	
