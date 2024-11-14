from tkinter import*
window = Tk()

name = Label(window,text="Name").grid(row=0,column=0)
e1 = Entry(window).grid(row=1,column=1)

password = Label(window,text="Password").grid(row=0,column=0)
e2 = Entry(window).grid(row=1,column=1)

submit = Button(window,text="Submit").grid(row=4,column=0)

window.mainloop()