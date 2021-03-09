from tkinter import *
from tkinter import messagebox
import random
import json
# search website in our database


def search():
    web_input = website_input.get()
    web_input = web_input.capitalize()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f"No Data File Found")

    else:
        if web_input.capitalize() in data:
            new_data = data[web_input]
            messagebox.showinfo(title=web_input,
                                message=f"Email-{new_data['email']}\n \n Password-{new_data['password']}")
        else:
            if len(web_input) > 0:
                messagebox.showinfo(title='Error', message=f"There is no Website present in this name {web_input}")
            else:
                messagebox.showinfo(title='Error', message='Fill the  Website name')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def password_generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web_input = website_input.get()
    web_input = web_input.capitalize()
    e_input = email_input.get()
    pass_input = password_input.get()
    new_data = {web_input: {'email': e_input, 'password': pass_input}}
    if len(web_input) > 0 and len(e_input) > 0 and len(pass_input) > 0:
        is_ok = messagebox.askokcancel(title=web_input,
                                       message=f'These are the details entered: \n Email: {e_input}\n password: {pass_input}')
        if is_ok:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            except json.decoder.JSONDecodeError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                email_input.delete(0, END)
                email_input.insert(0, '@gmail.com')
    else:
        messagebox.showinfo(title='Error', message="Please don't leave any field empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')
canvas = Canvas(width=400, height=300, highlightthickness=0)
image = PhotoImage(file='./logo.png')
canvas.create_image(200, 200, image=image)
canvas.config(bg='white')
canvas.grid(row=0, column=1)
website_label1 = Label(text='Website:', bg='white', font=('Arial', 13, 'bold'), pady=8)
website_label1.grid(row=1, column=0)
email_label = Label(text='Email/Username', bg='white', font=('Arial', 13, 'bold'), pady=8)
email_label.grid(row=2, column=0)
password_label = Label(text='Password', bg='white', font=('Arial', 13, 'bold'), pady=8)
password_label.grid(row=3, column=0)

website_input = Entry(width=49)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=70)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, '@gmail.com')

password_input = Entry(width=49)
password_input.grid(row=3, column=1)

search_button = Button(text='Search', bg='white', font=('Arial', 13, 'bold'), command=search, width=12)
search_button.grid(row=1, column=2)

password_gen_button = Button(text='Generate Password', bg='white', font=('Arial', 11, 'bold'), command=password_generator)
password_gen_button.grid(row=3, column=2)

add_button = Button(text='Add', width=68, bg='white', font=('Arial', 11, 'bold'), command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
