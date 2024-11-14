from tkinter import*
window = Tk()
window.geometry("415x250")

checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()

btn1 = Checkbutton(window,text="c",variable=checkVar1,onvalue=1,offvalue=1,height=2,width=10)
btn1.pack()

btn2 = Checkbutton(window,text="c++",variable=checkVar2,onvalue=1,offvalue=0,height=2,width=10)
btn2.pack()

btn3 = Checkbutton(window,text="java",variable=checkVar3,onvalue=1,offvalue=1,height=2,width=10)
btn3.pack()

window.mainloop()