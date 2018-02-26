# gamble.py
# gamble your money!!

#import the modules we need, for creating a GUI...
from tkinter import *
#...and for picking random names.
import random

class Window(Frame):

	def __init__(self, master=None):
		# parameters that you want to send through the Frame class. 
		Frame.__init__(self, master)   

		#reference to the master widget, which is the tk window                 
		self.master = master

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
		self.var.set("Ok, scale of 1 to 10, 10 being the highest, how much risk do we want to take on today?\n")
		self.outputLabel.pack()

		self.entry = Entry(self.master, width=10)
		self.entry.pack(side=TOP,padx=10,pady=10)

		Button(self.master, text='Enter', command=self.playGame).pack(side=LEFT)

		self.pack(fill=BOTH, expand=1)

	def playGame(self):
		print('test')

	#a function will determine the results of the game
	def playGame2(self):

		var.set("Ok, scale of 1 to 10, 10 being the highest, how much risk do we want to take on today?\n")
		outputLabel.pack()
		self.pack(fill=BOTH, expand=1)

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

		personOne = random.choice(names) #tuple1
		#names.remove(personOne) #prevents double picking
		personTwo = random.choice(names) #tuple2

		moneyOwed = riskLevel/10 * personOne[1]
		moneyOwedString = "%.2f" % moneyOwed

		message = personTwo[0] + ' won! ' + personOne[0] + ' lost :/ ... ' + personOne[0] +' owes ' + personTwo[0] + ' $' + moneyOwedString + '!'
		print(message)
		#nameLabel.configure(text=message)

	def client_exit(self):
		exit()

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
print('Thanks for playing! See you next time on... ')
print('\t\t\t\t\t\t\t...The Gambling Game!')
