from tkinter import *
import datetime

def add_income():
   new= Toplevel(root)
   new.geometry("360x100")
   new.title("Add Income")
   
   l1 = Label(new, text="Enter Pay Date (format is YYYY-MM-DD)").grid(row = 1, column = 0, sticky = W, pady = 2)
   l2 = Label(new, text="Enter Income Amount").grid(row = 2, column = 0, sticky = W, pady = 2)

   e1 = Entry(new)
   e1.grid(row=1, column=1, sticky=W, pady=2)
   e2 = Entry(new)
   e2.grid(row=2, column=1, sticky=W, pady=2)
   
   date = e1.get()
   income = e2.get()
   
   def run():
       tracker(201,income,0,0,0,0,0)
   
   submit = Button(new, text = "Save", bg = 'black', fg = 'white', width=15, command=run)
   submit.grid(row=3, column=1, sticky=W, pady=2)





root = Tk()
root.title('Monify - Expense Tracker Pro')
root.geometry("600x600")





logo_label = Label(root, text = 'MONIFY', font=('Century Gothic', 40))
logo_label.pack()


greet = Label(root, text="Welcome to Monify - The Best Expense Tracker App", font=('Century Gothic', 11))
greet.pack()

version_info = Label(root, text="Version 1.0.1.1\n\n\n\n\n\n\n\n\n\n\n", font=('Century Gothic', 7))
version_info.pack()


clicked = StringVar()
clicked.set("Select An Operation to Perform")

drop = OptionMenu(root, clicked, 'Enter Income', 'Plot Graph', 'Show Statistics')
drop.pack()


menu_click = Button(root, text = "Start", bg = 'black', fg = 'white', width=50, command=add_income).pack()
quit_button = Button(root, text = 'Exit', bg = 'red', fg = 'black', width = 50).pack()


root.mainloop()