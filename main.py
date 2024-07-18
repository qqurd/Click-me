from tkinter import*
from random import choice, randint
def press():
    colors = ['red', 'green', 'blue']
    btn.config(bg=choice(colors))
    btn.place(x=randint(0, 300), y=randint(0, 300))
window = Tk()


window.title("Кликер")
window.geometry('700x500')

btn = Button(text = 'Click me', font=('Arial', 20), command = press)
btn.place(x=0, y=0)

window.mainloop()