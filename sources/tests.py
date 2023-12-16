from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

counter=0
def changer():
    global counter
    counter+=1
    if counter%2==0:
        my_label.config(text='Hello World!')
    else:
        my_label.config(text='Nique Ta Mere!')
        

root=tb.Window(themename='superhero')
root.title('TTK Bootstrap')
root.title('TTK Bootstrap')
root.geometry('500x350')

my_label=tb.Label(text='Hello World!', font=('Helvetica',28),
                  bootstyle=DEFAULT)
my_label.pack(pady=50)

my_button=tb.Button(text='Click Me!', bootstyle='info, outline',command=changer)
my_button.pack(pady=20)

my_button=tb.Button(text='Click Me!', bootstyle='info, outline',command=changer)

root.mainloop()