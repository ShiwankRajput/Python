from tkinter import*
window = Tk()

redbutton = Button(window,text="red",fg="red")
redbutton.pack(side=TOP)

yellowbutton = Button(window,text="yellow",fg="yellow")
yellowbutton.pack(side=BOTTOM)

greenbutton = Button(window,text="green",fg="green")
greenbutton.pack(side=RIGHT)

blackbutton = Button(window,text="black",fg="black")
blackbutton.pack(side=LEFT)

window.mainloop()