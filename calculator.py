from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

a = e

#defining buttons

def myAdd():
    a = e.get()
    global a_num
    global math
    math = "addition"
    a_num = int(a)
    c = a_num
    e.delete(0, END)

def myEqual():
    if math == "addition":
        b = e.get()
        e.delete(0, END)
        e.insert(0, a_num + int(b))
    
    if math == "subtraction":
        b = e.get()
        e.delete(0, END)
        e.insert(0, a_num - int(b))
    
    if math == "division":
        b = e.get()
        e.delete(0, END)
        e.insert(0, int(a_num / int(b)))

    if math == "multiplication":
        b = e.get()
        e.delete(0, END)
        e.insert(0, a_num * int(b))

def myClear():
    e.delete(0, END)
    c = 0
    b = 0

def myClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def mySubtract():
    a = e.get()
    global a_num
    global math
    math = "subtraction"
    a_num = int(a)
    c = a_num
    e.delete(0, END)

def myMultiply():
    a = e.get()
    global a_num
    global math
    math = "multiplication"
    a_num = int(a)
    c = a_num
    e.delete(0, END)

def myDivide():
    a = e.get()
    global a_num
    global math
    math = "division"
    a_num = int(a)
    c = a_num
    e.delete(0, END)

#making buttons

myButton1 = Button(root, text="1", padx=10, pady=10, command=lambda: myClick(1))
myButton2 = Button(root, text="2", padx=10, pady=10, command=lambda: myClick(2))
myButton3 = Button(root, text="3", padx=10, pady=10, command=lambda: myClick(3))
myButton4 = Button(root, text="4", padx=10, pady=10, command=lambda: myClick(4))
myButton5 = Button(root, text="5", padx=10, pady=10, command=lambda: myClick(5))
myButton6 = Button(root, text="6", padx=10, pady=10, command=lambda: myClick(6))
myButton7 = Button(root, text="7", padx=10, pady=10, command=lambda: myClick(7))
myButton8 = Button(root, text="8", padx=10, pady=10, command=lambda: myClick(8))
myButton9 = Button(root, text="9", padx=10, pady=10, command=lambda: myClick(9))
myButton0 = Button(root, text="0", padx=10, pady=10, command=lambda: myClick(0))

myButtonSubtract = Button(root, text="-", padx=10, pady=10, command=mySubtract)
myButtonMultiply = Button(root, text="x", padx=10, pady=10, command=myMultiply)
myButtonDivide = Button(root, text="/", padx=10, pady=10, command=myDivide)
myButtonAdd = Button(root, text="+", padx=10, pady=10, command=myAdd)
myButtonEquals = Button(root, text="=", padx=10, pady=10, command=myEqual)
myButtonClear = Button(root, text="Clear", padx=10, pady=10, command=myClear)

myButton1.grid(row=3, column=0, sticky="ew")
myButton2.grid(row=3, column=1, sticky="ew")
myButton3.grid(row=3, column=2, sticky="ew")
myButton4.grid(row=2, column=0, sticky="ew")
myButton5.grid(row=2, column=1, sticky="ew")
myButton6.grid(row=2, column=2, sticky="ew")
myButton7.grid(row=1, column=0, sticky="ew")
myButton8.grid(row=1, column=1, sticky="ew")
myButton9.grid(row=1, column=2, sticky="ew")
myButtonAdd.grid(row=4, column=0, sticky="ew")
myButtonEquals.grid(row=4, column=1, sticky="ew")
myButton0.grid(row=4, column=2, sticky="ew")
myButtonClear.grid(row=6, sticky="ew", columnspan=3)
myButtonSubtract.grid(row=5, column=0, sticky="ew")
myButtonMultiply.grid(row=5, column=1, sticky="ew")
myButtonDivide.grid(row=5, column=2, sticky="ew")


root.mainloop()