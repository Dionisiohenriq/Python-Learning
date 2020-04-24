# Prompt the user to enter number / test if even or odd

question = input("Please enter a number: ")
number = int(question)

if number % 2 == 0:
	print("Your number is even.")
else:
	print("Your number is odd.")