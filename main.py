from tkinter import *

#Calculator GUI Window
root = Tk()
root.title("Calculator")
root.geometry('360x340+500+130')
root.resizable(0,0)
root.config(bg='gray')

#Enter box for calculation
var = StringVar()
en = Entry(
    root,
    font=('', 22),
    justify="right",
    textvariable=var,
)
en.place(x=15, y=10, height=55, width=333, )

#placing buttons
b = [Button()]*16
data = ('1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', 'x', 'C', '0', '=', '/')
k = 0
x = 15
y = 75
for i in range(4):
    for j in range(4):
        b[k] = Button(
            root,
            text=data[k],
            font=('', 20, 'bold'),
            height=1,
            width = 4,
            bg='light gray',
            fg='black',
            activebackground='light green',
        )
        b[k].place(x=x, y=y)
        k+=1
        x += 85
    x = 15
    y += 65
    
    
