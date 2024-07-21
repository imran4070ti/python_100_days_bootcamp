from tkinter import *


def miles_to_kilometers():
    distance_in_miles = float(entry_miles.get())
    distance_in_kilometers = 1.60934 * distance_in_miles
    label3.config(text = f'{distance_in_kilometers:.2f} KM')


window = Tk()
window.config(padx=50, pady=50)
window.minsize(height=300, width=500)
window.title('Miles to Kilometer converter')

# Miles entry
entry_miles = Entry(width=10, font=('Arial', 12, 'bold'))
entry_miles.insert(END, '0')
entry_miles.grid(row=0, column=1)

label1 = Label(text='Miles', font=('Arial', 12, 'bold'))
label1.grid(row=0, column=2)

label2 = Label(text='is equal to', font=('Arial', 12, 'bold'))
label2.grid(row=1, column=0)

label3 = Label(text='0', font=('Arial', 12, 'bold'))
label3.grid(row=1, column=1)

label4 = Label(text='KM', font=('Arial', 12, 'bold'))
label4.grid(row=1, column=2)

# Convert Button
button = Button(text='Calculate', width=10, command=miles_to_kilometers, font=('Arial', 12, 'bold'))
button.grid(row=2, column=1)






window.mainloop()