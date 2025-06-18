# python number guessing game 

import random

low_num = 1
high_num = 100
answer = random.randint( low_num , high_num )
guesses = 0
is_running = True

print(" Python Number Guessing Game ")
print(f"Select a number between {low_num} and {high_num} : ")

while is_running:
	
	guess = input("Enter your guess: ")

	if guess.isdigit():
		guess = int(guess)
		guesses += 1

		if guess < low_num or guess > high_num :
			print("That number is out of the range!!!")
			print(f" Please select a number between {low_num} and {high_num} : ")

		elif guess < answer:
			print("Too low! Try again!")

		elif guess > answer:
			print("Too high! Try again!")

		else:
			print(f"CORRECT !! The answer is {answer}")
			print(f"Number of guesses: {guesses} ")
			is_running = False

	else:
		print("Invalid guess")
		print(f" Please select a number between {low_num} and {high_num} : ")
