import tkinter as tk
from tkinter import ttk, scrolledtext

win = tk.Tk()

# adding a title
win.title("Python GUI")

# adding a label
aLabel = ttk.Label(win, text="Your name: ")
aLabel.grid(column=0, row=0)

def clickHandler():
	action.configure(text="* I have been clicked! *")
	aLabel.configure(foreground="red")
	aLabel.configure(text="Hello, " + name.get() + ", " + number.get())

# adding a input field
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# adding a label for select field
ttk.Label(win, text="Choose a number: ").grid(column=1, row=0)

# adding a select field
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 4, 5, 6, 7)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# adding first checkbox field
ch1 = tk.IntVar()
check1 = tk.Checkbutton(win, text="Option 1", variable=ch1)
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

# adding a disabled checkbox field
ch2 = tk.IntVar()
check2 = tk.Checkbutton(win, text="Disabled Option", variable=ch2, state="disabled")
check2.grid(column=1, row=2, sticky=tk.W)

# adding radio buttons
radVar = tk.IntVar()

COLOR1 = "Blue"
COLOR2 = "Green"

def radCall():
	radSel = radVar.get()
	# changes the background color of the application
	if radSel == 1: win.configure(background=COLOR1)
	if radSel == 2: win.configure(background=COLOR2)

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=3)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=3)

# adding a scrolled text control
scrollW = 30
scrollH = 3
scr = scrolledtext.ScrolledText(win, width=scrollW, height=scrollH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# adding a button
action = ttk.Button(win, text="Click me!", command=clickHandler)
action.grid(column=0, row=5)

# focus on input field
nameEntered.focus()

win.mainloop()