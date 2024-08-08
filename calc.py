import tkinter
from tkinter import *
from tkinter import messagebox

variable = ""
A = 0 
operator = ""

def button1_clicked():
    global variable
    variable =variable + "1"
    the_data.set(variable)

def button2_clicked():
    global variable
    variable =variable + "2"
    the_data.set(variable)

def button3_clicked():
    global variable
    variable =variable + "3"
    the_data.set(variable)

def button4_clicked():
    global variable
    variable =variable + "4"
    the_data.set(variable)

def button5_clicked():
    global variable
    variable =variable + "5"
    the_data.set(variable)

def button6_clicked():
    global variable
    variable =variable + "6"
    the_data.set(variable)

def button7_clicked():
    global variable
    variable =variable + "7"
    the_data.set(variable)

def button8_clicked():
    global variable
    variable =variable + "8"
    the_data.set(variable)

def button9_clicked():
    global variable
    variable =variable + "9"
    the_data.set(variable)

def button0_clicked():
    global variable
    variable =variable + "0"
    the_data.set(variable)

def buttonAdd_clicked():
    global A
    global variable
    global operator
    A = float(variable) 
    operator = "+"
    variable = variable + "+"
    the_data.set(variable)

def buttonSub_clicked():
    global A
    global variable
    global operator
    A = float(variable)
    operator = "-"
    variable = variable + "-"
    the_data.set(variable)

def buttonMul_clicked():
    global A
    global variable
    global operator
    A = float(variable)
    operator = "*"
    variable = variable + "*"
    the_data.set(variable)

def buttonDiv_clicked():
    global A
    global variable
    global operator
    A = float(variable)
    operator = "/"
    variable = variable + "/"
    the_data.set(variable)

def buttonEqual_clicked():
    global A
    global variable
    global operator
    A = float(variable)
    operator = "="
    variable = variable + "="
    the_data.set(variable)

def buttonC_clicked():
    global A
    global variable
    global operator
    A = 0 
    operator = ""    
    variable = ""
    the_data.set(variable)

def result():
    global A
    global variable
    global operator
    if operator == "+":
        a = float(variable.split("+")[1])
        x = A + a
        the_data.set(x)
        variable = str(x)
    elif operator == "-":
        a = float(variable.split("-")[1])
        x = A - a
        the_data.set(x)
        variable = str(x)
    elif operator == "*":
        a = float(variable.split("*")[1])
        x = A * a
        the_data.set(x)
        variable = str(x)
    elif operator == "/":
        a = float(variable.split("/")[1])
        if a == 0:
            messagebox.showerror("Error", "Division by zero")
            A == 0
            variable == ""
            the_data.set(variable)
        else:
            x = float(A / a)
            the_data.set(x)
            variable = str(x)

guiWindow = tkinter.Tk()
guiWindow.geometry("320x600+400+400")
guiWindow.resizable(0,0)
guiWindow.title("meyas calculator")

the_data = StringVar()
guiLabel= Label(guiWindow,
                 textvariable=the_data,
                text="Label" ,
                 font = ("Times New Roman", 20),
                 anchor= SE,
                background="#ffffff",
                fg = "#000000",
                )

guiLabel.pack(expand=1,fill= "both")

frame1 = Frame(guiWindow, bg="#000000")
frame1.pack(fill="both", expand=1)

frame2 = Frame(guiWindow, bg="#000000")
frame2.pack(fill="both", expand=1)

frame3 = Frame(guiWindow, bg="#000000")
frame3.pack(fill="both", expand=1)

frame4 = Frame(guiWindow, bg="#000000")
frame4.pack(fill="both", expand=1)

button1 = Button(
    frame1,
    text="1",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button1_clicked
)

button1.pack(side=LEFT, expand=1, fill="both")

button2 = Button(
    frame1,
    text="2",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button2_clicked
)

button2.pack(side=LEFT, expand=1, fill="both")

button3 = Button(
    frame1,
    text="3",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button3_clicked
)

button3.pack(side=LEFT, expand=1, fill="both")

buttonc = Button(
    frame1,
    text="C",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=buttonC_clicked
)

buttonc.pack(side=LEFT, expand=1, fill="both")

button4 = Button(
    frame2,
    text="4",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button4_clicked
)

button4.pack(side=LEFT, expand=1, fill="both")

button5 = Button(
    frame2,
    text="5",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button5_clicked
)

button5.pack(side=LEFT, expand=1, fill="both")

button6 = Button(
    frame2,
    text="6",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button6_clicked
)

button6.pack(side=LEFT, expand=1, fill="both")

buttonAdd = Button(
    frame2,
    text="+",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=buttonAdd_clicked
)

buttonAdd.pack(side=LEFT, expand=1, fill="both")

button7 = Button(
    frame3,
    text="7",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button7_clicked
)

button7.pack(side=LEFT, expand=1, fill="both")

button8 = Button(
    frame3,
    text="8",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button8_clicked
)

button8.pack(side=LEFT, expand=1, fill="both")

button9 = Button(
    frame3,
    text="9",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button9_clicked
)

button9.pack(side=LEFT, expand=1, fill="both")

buttonsub = Button(
    frame3,
    text="-",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=buttonSub_clicked
)

buttonsub.pack(side=LEFT, expand=1, fill="both")

button0 = Button(    
    frame3,
    text="0",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=button0_clicked
)

button0.pack(side=LEFT, expand=1, fill="both")

buttonMul = Button(
    frame4,
    text="*",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=buttonMul_clicked
)

buttonMul.pack(side=LEFT, expand=1, fill="both")

buttonDiv = Button(
    frame4,
    text="/",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command=buttonDiv_clicked
)

buttonDiv.pack(side=LEFT, expand=1, fill="both")

buttonEqual = Button(
    frame4,
    text="=",
    font=("Times New Roman", 22),
    relief=GROOVE,
    border=0,
    command= result
)

buttonEqual.pack(side=LEFT, expand=1, fill="both")  

guiWindow.mainloop()





