from tkinter import *

window = Tk()
window.title('My First GUI program')
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a label", font=('Times New Roman', 24, "bold"))
my_label.pack()
# my_label['text'] = 'New text'
my_label.config(text='New text set by config')



# Button
def button_clicked():
    text = input.get()
    my_label.config(text=text)
    
button = Button(text='Button', bg='blue', fg='red')
button['command'] = button_clicked
button.pack()


# Entry
input = Entry()
input.insert(END, 'Text Entry')
input.pack()


# Text Box
text_box = Text(width=10, height=7)
text_box.focus() # Put the cursor in the text box
text_box.insert(END, 'Example of multi-line text entry')
texts = text_box.get('1.0', END)
print(texts)
text_box.pack()

# Spinbox
def spinbox_used():
    # get the current value at the spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    # get the current value at the scale
    print(value)
scale = Scale(from_=0, to=10, width=10, command=scale_used)
scale.pack()


# Check Box
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# Radio Button
def radiobutton_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=radiobutton_used)
radiobutton2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=radiobutton_used)
radiobutton3 = Radiobutton(text='Option 3', value=3, variable=radio_state, command=radiobutton_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


# List Box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['Apple', 'Mango', 'Banana', 'Watermelon']
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()












window.mainloop()












# Handy Reference
# Setting options
"""
At object creation time
fred = Button(self, fg='red', bg='blue')

After object creation, treating the option name like a dictionary index
fred = Button()
fred['bg'] = 'blue'
fred['fg'] = 'red'

Use the config() method to update multiple attributes after creating the object
fred = Button()
fred.config(fg='red', bg='blue')
"""