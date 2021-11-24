from tkinter import *
from main import *


root = Tk()
root.title('Monify - Expense Tracker Pro')
root.geometry("500x500")




logo_label = Label(root, text = 'MONIFY', font=('Century Gothic', 40))
logo_label.pack()


greet = Label(root, text="Welcome to Monify - The Best Expense Tracker App\n\n", font=('Century Gothic', 11))
greet.pack()

version_info = Label(root, text="Version 1.0.1.1", font=('Century Gothic', 8))
version_info.pack()


clicked = StringVar
drop = OptionMenu(root, clicked, 'Enter income', 'Plot graph', 'Show statistics')
drop.pack()


root.mainloop()