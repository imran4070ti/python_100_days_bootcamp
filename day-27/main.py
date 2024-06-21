import tkinter as tk

window = tk.Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)

# Labellabel
my_label = tk.Label(text='I am a Label', font=('Arial', 24, 'bold'))  # To create a label on the window.
my_label.pack(side='left')  # To show the created label on the window.
















window.mainloop()  # Like a while loop that basically keeps the window open.