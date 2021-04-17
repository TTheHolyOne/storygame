# TTheHolyOne#1642
# Week one of me programming :) 
print('Hello there!\nWelcome to my story game! You enter the inputs and I make it into a story!\n')
input()
while True:
	


	name = input('Please enter a name! \n')
	age = int(input('Please enter a age! \n'))
	namefood = input('Please enter what you like to eat! \n')
	petname = input('Please enter your dogs name! \n')
	dogfood = input('Please enter what your dog likes to eat! \n')
	house = input('Please enter what you call your house! \n')

	option = input('Please enter what story you want to read \n 1 - Normal\n 2 - Strange\n')

	if option == '1':
		qp = input(f'My name is {name} and I am {age} years old. I have a dog named {petname}. My dog likes to eat {dogfood}. I love to eat {namefood}!\n I call my lovely house {house} \n\n Enter P to play again\n Enter Q to quit\n\n')
	elif option == '2':
		name=name.upper()
		namefood=namefood.upper()
		petname=petname.upper()
		dogfood=dogfood.upper()
		house=house.upper()
		qp = input(f'My nameee is {name} and I hunt and growl for {namefood}. I have A servant named {petname}.\nI eat {dogfood} with my dog at times... I live in a red place where I call {house}')
	if qp.lower() == 'q':
		break
	elif qp.lower() == 'p':
		continue
print('Shutting down...')