# Program to implement Rock Paper Scissor game 
import random

choices = ["rock", "paper", "scissor"]

user_score = 0
cpu_score = 0 

def setChoice():
	'''
		Function Takes character as input choice and return choice in string format if user press end then game overs and declares winner of the game 
	'''
	print("Press Choice chatacter :\n \"R\": ROCK \t \"P\": PAPER \n \"S\": SCISSOR \t \"E\": End Game")
	choice = input()

	if choice == "R" or choice == "r":
		return "rock"

	elif choice == "P" or choice == "p":
		return "paper"

	elif choice == "S" or choice == "s":
		return "scissor"

	elif choice == "E" or choice == "e":
		print("**Game Over**")
		printScore()
		if cpu_score > user_score:
			print("Final Winner : CPU")
		elif cpu_score == user_score:
			print("Tie")
		else:
			print("Final Winner : Player")
		exit()

	else:
			print("Worng Choice!..")
			printScore()
			exit()

def printScore():
	'''
		Function only prints the score of both players
	'''
	print(f"User Score : {user_score}\n CPU Score : {cpu_score}")

def updateScore():
	pass





if __name__ == '__main__':
	while True:
		user_choice = setChoice()

		if user_choice == "e":
			printScore()
			exit()

		cpu_choice = random.choice(choices)
		print(f"Your Choice : {user_choice.upper()}")
		print(f"CPU Choice : {cpu_choice.upper()}")

		if user_choice == cpu_choice:
			print("Tie")
			printScore()

		elif user_choice == "rock":
			if cpu_choice == "paper":
				print("You Lose! Paper covers Rock")
				cpu_score += 1
				printScore()
			else:
				print("You Won! Rock smashes Scissor")
				user_score += 1
				printScore()

		elif user_choice == "paper":
			if cpu_choice == "rock":
				print("You Won! Paper covers Rock")
				user_score += 1
				printScore()
			else:
				print("You lose! Scissor cuts paper")
				cpu_score += 1
				printScore()

		elif user_choice == "scissor":
			if cpu_choice == "paper":
				print("You Won! Scissor cuts paper")
				user_score += 1
				printScore()
			else:
				print("You Lose! Rock smashes scissor")
				cpu_score += 1
				printScore()
	   