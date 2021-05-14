from tkinter import *

root = Tk()
e = Entry(root, width=50, bg="gray", fg="black", borderwidth=5)
e.pack()

#Defining clicks / inputs

def Click():
    label1 = Label(root, text=e.get())
    label1.pack()

#Making a button, cause why not
button1 = Button(root, text="You're name", command=Click, fg="blue", bg="red")
button1.pack()

#Looping
root.mainloop()