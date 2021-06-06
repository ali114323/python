#Password Generator
import random
from tkinter import *

root = Tk()
amount = 8
#Functions
def generate():
    global amount
    g = e.get()
    amount = int(g)
    list = random.sample(numbers, amount)
    e.delete(0, END)
    e.insert(0, list)


#Widgets
myLabel1 = Label(root, text="Password generator!", padx=10, pady=10, )
myLabel2 = Label(root, text="Type in the amount of characters you want and press generate!", padx=10, pady=10, )
e = Entry(root)
myButton1 = Button(root, text="Generate", command=generate)
#Placing Widgets
myLabel1.grid(row=0, columnspan=1)
myLabel2.grid(row=1, columnspan=1)
myButton1.grid(row=3, columnspan=1)
e.grid(row=2, columnspan=1)

#Letters/Variables
numbers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","/","-","+","_"]
root.mainloop()
