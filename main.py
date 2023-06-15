from tkinter import *

def show(s):
    if en.get()=='Error':
        clear()
    var.set(en.get()+ s)
    
def clear():
    var.set('')

def cal():
    exp = en.get()
    if exp == '':
        var.set('')
    elif exp[-1]=='+' or exp[-1]=='-' or exp[0]=='*' or exp[0]=='/' or exp[-1]=='*' or exp[-1]=='/':
        var.set('Error')
    elif exp[-1]=='0' and exp[-2]=='/' or exp == 'Error':
        var.set('Error')
    elif '*/' in exp or '/*' in exp or '+*' in exp or '-*' in exp or '+/' in exp or '-/' in exp:
        var.set('Error') 
    elif exp[0]=='0':
        exp = exp[1:] 
        var.set(eval(exp))
    else:
        var.set(eval(exp))
        
   
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
    
#binding buttons with commands
b[0].config(command=lambda:show('1'))
b[1].config(command=lambda:show('2'))
b[2].config(command=lambda:show('3'))
b[3].config(command=lambda:show('+'))
b[4].config(command=lambda:show('4'))
b[5].config(command=lambda:show('5'))
b[6].config(command=lambda:show('6'))
b[7].config(command=lambda:show('-'))
b[8].config(command=lambda:show('7'))
b[9].config(command=lambda:show('8'))
b[10].config(command=lambda:show('9'))
b[11].config(command=lambda:show('*'))
b[12].config(command=clear)
b[13].config(command=lambda:show('0'))
b[14].config(command=cal)
b[15].config(command=lambda:show('/'))

root.mainloop()
