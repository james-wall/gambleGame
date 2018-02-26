# gamble.py
# gamble your money!!

#import the modules we need, for creating a GUI...
import tkinter
#...and for picking random names.
import random

#a function will determine the results of the game
def playGame(riskLevel):
	# todo add logic for keeping between 1 and 10

	personOne = random.choice(names) #tuple1
	#names.remove(personOne) #prevents double picking
	personTwo = random.choice(names) #tuple2

	moneyOwed = riskLevel/10 * personOne[1]
	moneyOwedString = "%.2f" % moneyOwed

	message = personTwo[0] + ' won! ' + personOne[0] + ' lost :/ ... ' + personOne[0] +' owes ' + personTwo[0] + ' $' + moneyOwedString + '!'
	print(message)
	#nameLabel.configure(text=message)

print('Oh hai there')
print('Welcome to the world-renowned gambling emporium festivus:')
print('The Gambling Game!\n\n')

# Get number of people participating
num = int(input('So how many people do we have participating with us on this fine day?\n')) # todo add try catch for invalid input and negative input

print('Fantastic!')

#the list of possible names.
names = []

for i in range (0, num):
	personNum = i + 1
	personName = str(input('Who\'s person number ' + str(personNum) + '?')) # todo add try/catch
	print('Worddddd\n')
	personMoney = int(input('So how much money does ' + personName + ' have with them?\n'))
	# todo add joke based on money amount
	print('Let\'s here it for Contestant #' + str(personNum) + ', ' + personName + '!\n\n\n')
	personTuple = (personName, personMoney)
	names.append(personTuple)

if len(names) < 1:
	throw #add throw logic

riskLevel = int(input("Ok, scale of 1 to 10, 10 being the highest, how much rish do we want to take on today?\n"))

playGame(riskLevel)


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