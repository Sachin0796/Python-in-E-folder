from tkinter import *

root = Tk()
frame = Frame(root)

def submitValue():
    myValue = e1.get()
    myValue2 = e2.get()
    print(myValue + " " + myValue2)

# T = Text(root, height=2, width=30)
# T.grid(row=0,column=0)
# T.insert(END,'')
# T2 = Text(root, height=2, width=30)
# T2.grid(row=0,column=1)
# T2.insert(END,'')

Label(root, text='First Name').grid(row=0)
Label(root, text='Last Name').grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

button = Button(root, text="Submit", width = 25, command=lambda: submitValue())

button.grid(row=2, column=0)
frame.grid()

frame.mainloop()