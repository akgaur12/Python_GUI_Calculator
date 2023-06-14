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
