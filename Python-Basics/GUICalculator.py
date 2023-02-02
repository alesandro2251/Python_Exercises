from tkinter import *
import math

x = ""

def press(num):
    global x
    x = x + str(num)
    n.set(x)


def equalpress():
    try:
        global x
        total = str(eval(x))
        n.set(total)
        x = ""
    except:
        n.set(" error ")
        x = ""


def clear():
    global x
    x = ""
    n.set("")


a = Tk()
a.configure(background="black")
a.title("GUI Calculator")
a.geometry("450x300")

n = StringVar()
x_field = Entry(a, textvariable=n)
x_field.grid(columnspan=10, ipadx=120)

button1 = Button(a, text=' 1 ', bg='white', command=lambda: press(1), height=3, width=15)
button1.grid(row=2, column=0)

button2 = Button(a, text=' 2 ', bg='white', command=lambda: press(2), height=3, width=15)
button2.grid(row=2, column=1)

button3 = Button(a, text=' 3 ', bg='white', command=lambda: press(3), height=3, width=15)
button3.grid(row=2, column=2)

button4 = Button(a, text=' 4 ', bg='white', command=lambda: press(4), height=3, width=15)
button4.grid(row=3, column=0)

button5 = Button(a, text=' 5 ', bg='white', command=lambda: press(5), height=3, width=15)
button5.grid(row=3, column=1)

button6 = Button(a, text=' 6 ', bg='white', command=lambda: press(6), height=3, width=15)
button6.grid(row=3, column=2)

button7 = Button(a, text=' 7 ', bg='white', command=lambda: press(7), height=3, width=15)
button7.grid(row=4, column=0)

button8 = Button(a, text=' 8 ', bg='white', command=lambda: press(8), height=3, width=15)
button8.grid(row=4, column=1)

button9 = Button(a, text=' 9 ', bg='white', command=lambda: press(9), height=3, width=15)
button9.grid(row=4, column=2)

button0 = Button(a, text=' 0 ', bg='white', command=lambda: press(0), height=3, width=15)
button0.grid(row=5, column='1')

addition = Button(a, text=' + ', bg='white', command=lambda: press("+"), height=3, width=15)
addition.grid(row=2, column=3)

subtraction = Button(a, text=' - ', bg='white', command=lambda: press("-"), height=3, width=15)
subtraction.grid(row=3, column=3)

multiplication = Button(a, text=' * ', bg='white', command=lambda: press("*"), height=3, width=15)
multiplication.grid(row=4, column=3)

division = Button(a, text=' / ', bg='white', command=lambda: press("/"), height=3, width=15)
division.grid(row=5, column=3)

rooting = Button(a, text='√', bg='white', command=lambda: press(math.sqrt()), height=3, width=15)
rooting.grid(row=6, column=3)

result = Button(a, text=' = ', bg='light green', command=equalpress, height=3, width=15)
result.grid(row=6, column=2)

Clear = Button(a, text='Clear', bg='red', command=clear, height=3, width=15)
Clear.grid(row=6, column=0)

dot = Button(a, text='.', bg='white', command=lambda: press('.'), height=3, width=15)
dot.grid(row=5, column=2)

multiplication_1 = Button(a, text='+/-', bg='white', command=lambda: press('* -1'), height=3, width=15)
multiplication_1.grid(row=5, column=0)

a.mainloop()
