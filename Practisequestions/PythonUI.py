from tkinter import *

root = Tk()
frame = Frame(root)

def submitValue():
    myValue = e1.get()
    myValue2 = e2.get()
    myValue3 = clickedItem.get()
    print(myValue + " bought " +  myValue3 )

Label(root, text='First Name').grid(row=0, column=0)
Label(root, text='Address').grid(row=0, column=3)
Label(root, text='Phone number').grid(row=1, column=0)
Label(root, text='Item').grid(row=1, column=3)
Label(root, text='Model').grid(row=2, column=0)
Itemoptions = [
    "LED TV",
    "Washing machine",
    "Refridgerator"
]

modelOptions={
    "LED TV":["32","40","43"],
    "Washing machine":[8,8.5,9]
}


clickedItem = StringVar()
clickedItem.set( "LED TV" )

clickedModel = StringVar()
clickedModel.set("32")

Label(root, text='Item').grid(row=1, column=3)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
dropItem = OptionMenu( root, clickedItem , *Itemoptions )
dropModel = OptionMenu( root, clickedModel , *modelOptions )
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
dropItem.grid(row=1, column=4)
dropModel.grid(row=2, column=1)

button = Button(root, text="Submit", width = 25, command=lambda: submitValue())

button.grid(row=3, column=2)
frame.grid()

frame.mainloop()