# gamble.py
# gamble your money!!

#import the modules we need, for creating a GUI...
from tkinter import *
#...and for picking random names.
import random

gameStep = 0
riskLevel = 0
numPeople = 0
personIndex = 0
names = []

class Window(Frame):

	def __init__(self, master=None):
		# parameters that you want to send through the Frame class. 
		Frame.__init__(self, master)   

		#reference to the master widget, which is the tk window                 
		self.master = master

		global gameStep
		global riskLevel
		global numPeople
		global names
		global personIndex

		text = '\n\nOh hai there\n'
		text += 'Welcome to the world-renowned gambling emporium festivus:\n'
		text +=  'The Gambling Game!\n'

		#add a label for displaying the name.
		self.nameLabel = Label(self.master, text=text)
		self.nameLabel.place(x = 500, y = 0)
		self.nameLabel.pack()

		self.var = StringVar()
		self.outputLabel = Label(self.master, textvariable = self.var)
		self.outputLabel.place(x = 500, y = 500)
		self.outputLabel.pack()

		#with that, we want to then run init_window, which doesn't yet exist
		self.init_window()

	#Creation of init_window
	def init_window(self):

		# changing the title of our master widget      
		self.master.title("GUI")

		# allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)

		# creating a button instance
		playButton = Button(self, text="Play Game!", command=self.playGameInit)
		quitButton = Button(self, text="Quit", command=self.client_exit)

		# placing the button on my window
		playButton.place(x=0, y=0)
		quitButton.place(x=100, y=0)	

	def playGameInit(self):
		self.var.set('So how many people do we have participating with us on this fine day?\n')
		self.outputLabel.pack()

		self.entry = Entry(self.master, width=10)
		self.entry.pack(side=TOP,padx=10,pady=10)

		Button(self.master, text='Enter', command=self.playGame).pack(side=LEFT)

		self.pack(fill=BOTH, expand=1)

	def getNumPeople(self):
		global numPeople
		global gameStep
		global personIndex

		try:
			# Get number of people participating
			numPeople = int(str(self.entry.get())) # todo add try catch for invalid input and negative input
			if numPeople < 2:
				self.var.set('There needs to be at least two people in order to play the game!')
		except (ValueError, TypeError):
			self.var.set('You need to give me at least two people\'s names to play the game!\n Please try again.')

		self.var.set('Fantastic!\n\n, Now Who\'s person number ' + str(personIndex + 1) + '?\n')
		gameStep = 1

	def getPersonName(self):
		global numPeople
		global gameStep
		global names

		try:
			personName = str(self.entry.get())
			self.var.set('Worddddd\n So how much money does ' + personName + ' have with them?\n')
		except (ValueError, TypeError):
			print('Please give a name') 
		personValue = [personName, 0]
		names.append(personValue)
		print('personIndex ' + str(personIndex) + ', length: ' + str(len(names)))

	def getPersonMoney(self):
		global numPeople
		global gameStep
		global names
		global personIndex

		personMoney = 0

		try:
			personMoney = int(str(self.entry.get()))
		except (ValueError, TypeError):
			self.var.set('Please give me a monetary value') 

		print('personIndex ' + str(personIndex) + ', length: ' + str(len(names)))
		names[personIndex][1] = personMoney

		if personIndex  < numPeople - 1:
			# todo add joke based on money amount
			self.var.set('Let\'s here it for Contestant #' + str(personIndex + 1) + ', ' + names[personIndex][0] + '!\n\n\n Now who\'s next?')
			personIndex += 1
			gameStep = 1
		else:
			self.var.set("Ok, scale of 1 to 10, 10 being the highest, how much risk do we want to take on today?\n")
			gameStep = 3

	def getRiskLevel(self):
		global gameStep
		try:
			riskLevel = int(str(self.entry.get()))
			if riskLevel > 10 or riskLevel < 1:
				self.var.set('Sorry champ, try again. You need to give me a risk level between 1 and 10 (inclusive). Please try again')
				raise ValueError
		except (ValueError, TypeError) as error:
			self.var.set(str(error) + 'Invalid type of input. We need an integer between 1 and 10 (inclusive) Please try again.')
		self.var.set('Alright, it\'s game time!')

	#a function will determine the results of the game
	def gameTime(self):

		global names
		global riskLevel
		global gameStep

		personOne = random.choice(names) #tuple1
		#names.remove(personOne) #prevents double picking
		personTwo = random.choice(names) #tuple2

		moneyOwed = riskLevel/10 * personOne[1]
		moneyOwedString = "%.2f" % moneyOwed

		message = personTwo[0] + ' won! ' + personOne[0] + ' lost :/ ... ' + personOne[0] +' owes ' + personTwo[0] + ' $' + moneyOwedString + '!\n\n Thanks for playing!\n\n (press enter one more time to exit)'

		self.var.set(message)
		gameStep = 4

	def client_exit(self):
		exit()

	def playGame(self):

		global personIndex
		global gameStep
		print('We are starting on step: ' + str(gameStep)) # For testing purposes

		if gameStep == 0:
			self.getNumPeople()
		elif gameStep == 1:
			self.getPersonName()
			gameStep = 2
		elif gameStep == 2:
			self.getPersonMoney()
		elif gameStep == 3:
			self.getRiskLevel()
			self.gameTime()
		elif gameStep == 4:
			self.client_exit()
		else:
			self.var.set('Something went wrong')

		print('We are ending on step: ' + str(gameStep)) # For testing purposes

#create a GUI window.
root = Tk()
#set the title.
root.title("The Gambling Game!")
#set the size.
root.geometry("800x600")
app = Window(root)

# #add a 'pick name' button
# pickButton = tkinter.Button(text="Play Game!", command=playGame(riskLevel))
# pickButton.pack()

#start the GUI
root.mainloop()