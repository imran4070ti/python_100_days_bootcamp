from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
data = {
    'lower':['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    'upper':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    'digits':['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    'characters':['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+']
}
keys = ['lower', 'upper', 'digits', 'characters']

def password_generator():
    password_entry.delete(0, END)
    password_chars = []
    length = 13
    all_chars = []
    random.shuffle(keys)
    for key in keys:
        chars = data[key]
        all_chars.extend(chars)
        password_chars.append(chars[random.randint(0, len(chars)-1)])
    remaining = length - len(password_chars)
    while remaining>0:
        password_chars.append(all_chars[random.randint(0, len(all_chars)-1)])
        remaining-= 1
    password = ''
    random.shuffle(password_chars)
    for char in password_chars:
        password += char
    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website:{
            'email':email,
            'password':password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Opps', message='Please do not leave any entry empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?')
        if is_ok:
            try:
                with open('day-30/password_manager/data.json', 'r') as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = {} 
            except FileNotFoundError:
                with open('day-30/password_manager/data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data[website] = new_data[website]
                # data.update(new_data)
                with open('day-30/password_manager/data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                password_entry.delete(0, END)
                website_entry.delete(0, END)
                messagebox.showinfo(title=website, message='Details saved successfully.')

# ---------------------------- SEARCHING MECHANISM ------------------------------- #
def search():
    website = website_entry.get()
    print(website)
    try:
        with open('day-30/password_manager/data.json', 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                messagebox.showerror(title='Opps', message='Data not found')
            else:
                if website in data:
                    email = data[website]['email']
                    password = data[website]['password']
                    messagebox.showinfo(title='Found', message=f'Email: {email}\nPassword: {password}')
                else:
                    messagebox.showerror(title='Opps', message='Data not found')
    except FileNotFoundError:
        messagebox.showerror(title='Opps', message='Data not found')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='day-30/password_manager//logo.png')
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column=1, sticky='w')

# Website Label and Entry Box
website_label = Label(text='Website:')
website_label.grid(row=1, column=0, sticky='w')

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')

# # Seaerch button
search_button = Button(text='Search', command=search)
search_button.grid(row=1, column=2, sticky='e')

# Email/Username Label and Entry Box
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0, sticky='w')

email_entry = Entry(width=44)
email_entry.insert(0, 'example@email.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky='w')

# Password Label, Entry Box and Generate Password Button
password_label = Label(text='Password:')
password_label.grid(row=3, column=0, sticky='w')

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1, columnspan=2,  sticky='w')

generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(row=3, column=1, columnspan=2, sticky='e')

# Add button
add_button = Button(text='Add', width=37, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()