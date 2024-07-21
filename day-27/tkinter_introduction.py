from tkinter import *

def button_clicked():
    text = input.get()
    my_label.config(text=text)

window = Tk()
window.title('My First GUI program')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


# Label
my_label = Label(text="I am a label", font=('Times New Roman', 12, "bold"))
my_label.config(text='New text set by config')

# Button
button = Button(text='Button', bg='blue', fg='red')
button['command'] = button_clicked

button2 = Button(text='New Button')

# Entry
input = Entry()
input.insert(END, 'Text Entry')





my_label.grid(row=0, column=0)
button.grid(row=1, column=1)
button2.grid(row=0, column=2)
input.grid(row=2, column=3)



window.mainloop()










"""
Tkinter Layout Manager
Pack-> Packs all the weigts next to each other in a vaguely logical format. By default pack starts from top
and then pack every other widgets just below the previous one. Using pack layout manager, sometimes it's very
difficult to arrange the widgets.

Place-> Place is all about precise positioning. It use x,y cordinates to position a widgets. But the problem
place is it's so specific and not responsive.

Grid-> Divide the window to row and columns and you can specify the position of the widgets by using specific
row and column.
"""