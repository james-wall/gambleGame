# gamble.py
# gamble your money!!

#import the modules we need, for creating a GUI...
import tkinter
#...and for picking random names.
import random
try:
	#a function will determine the results of the game
	def playGame(riskLevel):
		if riskLevel > 10 or riskLevel < 1:
			print('Sorry champ, try again. You need to give me a risk level between 1 and 10 (inclusive)')
			return

		personOne = random.choice(names) #tuple1
		#names.remove(personOne) #prevents double picking
		personTwo = random.choice(names) #tuple2

		moneyOwed = riskLevel/10 * personOne[1]
		moneyOwedString = "%.2f" % moneyOwed

		message = personTwo[0] + ' won! ' + personOne[0] + ' lost :/ ... ' + personOne[0] +' owes ' + personTwo[0] + ' $' + moneyOwedString + '!'
		print(message)
		#nameLabel.configure(text=message)

	print('\n\nOh hai there')
	print('Welcome to the world-renowned gambling emporium festivus:')
	print('The Gambling Game!\n')
	print('(Press Ctrl-C at any time to exit the game)\n\n')

	num = 0 
	tryAgain = False;
	while True:
		try:
			# Get number of people participating
			num = int(input('So how many people do we have participating with us on this fine day?\n')) # todo add try catch for invalid input and negative input
			if num < 2:
				print('There needs to be at least two people in order to play the game!')
				pass
			break
		except (ValueError, TypeError):
			print('You need to give me at least two people\'s names to play the game!')
			print('Please try again\n')
			pass
		print('Input is invalid, please try again')

	print('Fantastic!')

	#the list of possible names.
	names = []

	for i in range (0, num):
		while True:
			try:
				personNum = i + 1
				personName = str(input('Who\'s person number ' + str(personNum) + '?\n')) # todo add try/catch
				print('Worddddd\n')
				personMoney = int(input('So how much money does ' + personName + ' have with them?\n'))
				# todo add joke based on money amount
				print('Let\'s here it for Contestant #' + str(personNum) + ', ' + personName + '!\n\n\n')
				personTuple = (personName, personMoney)
				names.append(personTuple)
				break           
			except (ValueError, TypeError):
				print('Please give a name and a money value.')   
				pass
			print('\nIncorrect type of input, please try again')

	try:
		if len(names) < 2:
			raise  ValueError('You need to give me at least two people\'s names to play the game!')
	except ValueError as error:
		print(str(error))

	while True:
		try:
			riskLevel = int(input("Ok, scale of 1 to 10, 10 being the highest, how much risk do we want to take on today?\n"))
			if riskLevel > 10 or riskLevel < 1:
				print('Sorry champ, try again. You need to give me a risk level between 1 and 10 (inclusive)')
				pass
			break
		except (ValueError, TypeError):
			print('Invalid input, please try again.')
			pass
		print ('\nIncorrect type of input, please try again')
	
	playGame(riskLevel)

except (KeyboardInterrupt):
	print('Thanks for playing! See you next time on... ')
	print('\t\t\t\t\t\t\t...The Gambling Game!')


# #create a GUI window.
# root = tkinter.Tk()
# #set the title.
# root.title("The gamble game")
# #set the size.
# root.geometry("200x100")

# #add a label for displaying the name.
# nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
# nameLabel.pack()

# #add a 'pick name' button
# pickButton = tkinter.Button(text="Play Game!", command=playGame(riskLevel))
# pickButton.pack()

# #start the GUI
# root.mainloop()