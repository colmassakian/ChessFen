from ChessFEN import *
from Tkinter import *
import webbrowser

def submit(): 
	link = linkEntry.get()
	fen = getFEN(link)
	selection = "https://lichess.org/analysis/standard/" + fen + "_" + color.get() + "_KQkq_-_0_1"
	print(selection)
	resultLink.config(text = selection)
	resultLink.bind("<Button-1>", lambda event: webbrowser.open(selection, new = 1))


root = Tk()
root.geometry("1000x400") 
color = StringVar(value="w")
linkEntry = StringVar()

L1 = Label(root, text="Enter link")
E1 = Entry(root, textvariable = linkEntry)


chooseLabel = Label(root)
chooseLabel.config(text = "Which piece to move?")

R1 = Radiobutton(root, text="White", variable=color, value="w")
R2 = Radiobutton(root, text="Black", variable=color, value="b")

# TODO: Bind to enter key
submitButton = Button(root, text = 'Submit', command = submit)

resultLink = Label(root)

L1.grid(row=0,column=0) 
E1.grid(row=0,column=1) 
chooseLabel.grid(row=3,column=0) 
R1.grid(row=3,column=1)
R2.grid(row=3,column=2) 
submitButton.grid(row=5,column=1)
resultLink.grid(row=7,column=1)
root.mainloop()