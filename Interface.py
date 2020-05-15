from ChessFEN import *
from Tkinter import *
import webbrowser

# def callback(url):
# 	print(url)
#     webbrowser.open_new(url)

def submit(): 
	link = linkEntry.get()
	fen = getFEN(link)
	selection = "https://lichess.org/analysis/standard/" + fen + "_" + color.get() + "_KQkq_-_0_1"
	print(selection)
	label.config(text = selection)
	label.bind("<Button-1>", lambda event: webbrowser.open(selection, new = 1))


root = Tk()
root.geometry("1000x400") 
color = StringVar(value="w")
linkEntry = StringVar()

L1 = Label(root, text="Enter link")
# L1.pack( side = LEFT)
E1 = Entry(root, textvariable = linkEntry)
# E1.pack(side = RIGHT)


chooseLabel = Label(root)
# chooseLabel.pack()
chooseLabel.config(text = "Which piece to move?")

R1 = Radiobutton(root, text="White", variable=color, value="w")
# R1.pack( anchor = W )

R2 = Radiobutton(root, text="Black", variable=color, value="b")
# R2.pack( anchor = W )

submitButton = Button(root, text = 'Submit', command = submit)
# submitButton.pack()


label = Label(root)
# label.pack()

L1.grid(row=0,column=0) 
E1.grid(row=0,column=1) 
chooseLabel.grid(row=3,column=0) 
R1.grid(row=3,column=1)
R2.grid(row=3,column=2) 
submitButton.grid(row=5,column=1)
label.grid(row=7,column=1)
root.mainloop()