from tkinter import*
window = Tk()
window.title("Entry page")
window.geometry("400x250")

name = Label(window,text="Name").place(x=30,y=50)
e1 = Entry(window).place(x=90,y=50)

password = Label(window,text="Password").place(x=30,y=80)
e2 = Entry(window).place(x=90,y=80)

email = Label(window,text="Email").place(x=30,y=110)
e3 = Entry(window).place(x=90,y=110)

submit = Button(window,text="Submit").place(x=30,y=140)

window.mainloop()