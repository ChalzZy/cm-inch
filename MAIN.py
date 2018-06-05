# Charles Monaghan | conversion calculator (cm - inches)

# imports tkinter module
from tkinter import *
from tkinter import ttk

# base code for making the code work
def calculator(*args):
        try:
            value = float(cm.get())
            inches.set(value * 0.39370)
        except ValueError:
            pass

# generates a basic window
root = Tk()
# makes the title of the programm "cm to inches"    
root.title("cm to inches")

#creates padding for the program
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# stores StringVar() into a easy to remember variable
cm = StringVar()
inches = StringVar()

# creates a user input window
cm_entry = ttk.Entry(mainframe, width=7, textvariable=cm)
cm_entry.grid(column=2, row=1, sticky=(W, E))

# makes a user friendly spot for the answer to be displayed
password_entry = ttk.Entry(mainframe, width=7, textvariable=cm)
password_entry.grid(column=2, row=2, sticky=(W, E))

# creates "calculate" button and uses the calculator function
ttk.Label(mainframe, textvariable=inches).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculator).grid(column=3, row=3, sticky=W)

# labeling for the text in the program
ttk.Label(mainframe, text="cm").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="inches").grid(column=3, row=2, sticky=W)

# ensures that all of the padding is even and user friendly
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

cm_entry.focus()
root.bind('return', calculator)

root.mainloop()
