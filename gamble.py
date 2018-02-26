# gamble.py
# gamble your money!!

#import the modules we need, for creating a GUI...
import tkinter
#...and for picking random names.
import random

print('Oh hai there')
print('Welcome to the world-renowned gambling emporium festivus:')
print('The Gambling Game!')

# Get number of people participating
print('So how many people do we have participating with us on this fine day?') #todo add time functionality to determine if they say day or evening
num = int(input()) # todo add try catch for invalid input and negative input

print('Fantastic!')

#the list of possible names.
names = []

for i in range (0, input()):
	personNum = i + 1
	print('Who\'s person number ' + str(personNum) + '?')
	personName = str(input()) # todo add try/catch
	print('Worddddd')
	personMoney = input('So how much money does ' + personName + ' have with them?')
	# todo add joke based on money amount
	print('Let\'s here it for Contestant #' + personNum + ', ' + personName + '!')
	personTuple = (personName, personMoney)
	names.append(personTuple)

if len(names) < 1:
	throw #add throw logic

#a function will determine the results of the game
def playGame():
	riskLevel = int(input("Ok, scale of 1 to 10, 10 being the highest, how risky are we feeling today?"))
	# todo add logic for keeping between 1 and 10

	personOne = random.choice(names) #tuple1
	#names.remove(personOne) #prevents double picking
	personTwo = random.choice(names) #tuple2

	moneyOwed = riskFactor/10 * personOne.index(1)

	message = personTwo.index(0) + ' won! ' + personOne.index(0) + ' lost :/ ... ' + personOne.index(0) +' owes ' + personTwo.index(0) + ' $' + moneyOwed + '!'
    nameLabel.configure(text=message)

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("The gamble game")
#set the size.
root.geometry("200x100")

#add a label for displaying the name.
nameLabel = tkinter.Label(root, text="", font=('Helvetica', 32))
nameLabel.pack()

#add a 'pick name' button
pickButton = tkinter.Button(text="Play Game!", command=playGame)
pickButton.pack()

#start the GUI
root.mainloop()