from tkinter import *
from tkinter import messagebox

# Creates the window
clicker = Tk()

# Assigns the window a title, size,background colour, and position on the screen
clicker.title('Clicker')
clicker.geometry('150x100')
clicker.configure(bg='lightgray')
winWidth = clicker.winfo_reqwidth()
winwHeight = clicker.winfo_reqheight()
posRight = int(clicker.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(clicker.winfo_screenheight() / 2 - winwHeight / 2)
clicker.geometry('+{}+{}'.format(posRight, posDown))

# Creates a counter for the clicker
clicker.counter = 0

# Adds to the counter for the clicker
def clicked():
    clicker.counter += 1
    L['text'] = 'button clicked: ' + str(clicker.counter)

# Creates the button you click
b = Button(clicker,text = 'click me', command=clicked)
b.pack()

# Creates the design for the counter
L = Label(clicker, text='no clicks yet')
L.pack(side = BOTTOM)

clicker.mainloop()