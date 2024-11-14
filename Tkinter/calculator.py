from tkinter import*

expression = ""

def press(num):
    global expression
    expression = expression+str(num)
    equation.set(expression)

def clear():
    global expression
    expression=""
    equation.set("")    

def equalpress():
    try:
        global expression
        total= str(eval(expression))
        equation.set(total)
        expression=""

    except:
        equation.set("error")
        expression=""    

if __name__ =="__main__":        

    window = Tk()
    window.geometry("270x150")
    # window.configure(background="black")

    equation = StringVar()

    expression_field = Entry(window, textvariable=equation).grid(columnspan=4,ipadx=70)

    window.title("simple calculator")

    Button1 = Button(window,text="1",fg="black",bg="skyblue",command=lambda: press(1),height=1,width=5).grid(row=2,column=0)

    Button2 = Button(window,text="2",fg="black",bg="skyblue",command=lambda: press(2),height=1,width=5).grid(row=2,column=1)

    Button3 = Button(window,text="3",fg="black",bg="skyblue",command=lambda: press(3),height=1,width=5).grid(row=2,column=2)

    Button4 = Button(window,text="4",fg="black",bg="skyblue",command=lambda: press(4),height=1,width=5).grid(row=3,column=0)

    Button5 = Button(window,text="5",fg="black",bg="skyblue",command=lambda: press(5),height=1,width=5).grid(row=3,column=1)

    Button6 = Button(window,text="6",fg="black",bg="skyblue",command=lambda: press(6),height=1,width=5).grid(row=3,column=2)

    Button7 = Button(window,text="7",fg="black",bg="skyblue",command=lambda: press(7),height=1,width=5).grid(row=4,column=0)

    Button8 = Button(window,text="8",fg="black",bg="skyblue",command=lambda: press(8),height=1,width=5).grid(row=4,column=1)

    Button9 = Button(window,text="9",fg="black",bg="skyblue",command=lambda: press(9),height=1,width=5).grid(row=4,column=2)

    Button0 = Button(window,text="0",fg="black",bg="skyblue",command=lambda: press(0),height=1,width=5).grid(row=5,column=0)

    plus = Button(window,text="+",fg="black",bg="skyblue",command=lambda: press("+"),height=1,width=5).grid(row=2,column=3)

    minus = Button(window,text="-",fg="black",bg="skyblue",command=lambda: press("-"),height=1,width=5).grid(row=3,column=3)

    multiply = Button(window,text="x",fg="black",bg="skyblue",command=lambda: press("x"),height=1,width=5).grid(row=4,column=3)

    divide = Button(window,text="/",fg="black",bg="skyblue",command=lambda: press("/"),height=1,width=5).grid(row=5,column=3)

    clear = Button(window,text="clear",fg="black",bg="skyblue",command=clear,height=1,width=5).grid(row=5,column=1)

    equals_to = Button(window,text="=",fg="black",bg="skyblue",command=equalpress,height=1,width=5).grid(row=5,column=2)

    decimal = Button(window,text=".",fg="black",bg="skyblue",command=lambda: press("."),height=1,width=5).grid(row=6,column=0)


    window.mainloop()