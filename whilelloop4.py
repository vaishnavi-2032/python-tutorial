#while loop guessing game

import random


def guessNumber(number) :
	ans = int(input('Enter number '))
	if(ans==number):
		print('You Won!!')
		askuser()
	elif(ans<number):
		print('Guess greater number')
		guessNumber(number)
	elif(ans>number):
		print('Guess lesser number')
		guessNumber(number)
		
def askuser():
	number = int(random.random()*100 + random.random()*10)
	print('Do you want to play? Enter y for yes and n for no')
	res = input()
	if res=='y':
		guessNumber(number)
	elif res=='n':
		print('Bye')
	else:
		print('Enter y or n only')
		askuser()

askuser()		

		
		

