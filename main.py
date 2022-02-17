from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from typing import final
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_in.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = web_in.get()
    email = user_in.get()
    password = pass_in.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_in.delete(0, END)
            pass_in.delete(0, END)

# ---------------------------- FIND INFO ------------------------------- #
def find_info():
    website = web_in.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if data[website]:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) 
canvas.grid(column=1, row=0)

# Labels 
web_label = Label(text="Website:", padx= 8)
user_label = Label(text="Email/Username:", padx= 8)
pass_label = Label(text="Password:", padx= 8)
web_label.grid(column=0, row=1)
user_label.grid(column=0, row=2)
pass_label.grid(column=0, row=3)

# Entry
web_in = Entry()
user_in = Entry()
pass_in = Entry()
web_in.grid(column=1, row=1, columnspan=2, sticky="EW")
user_in.grid(column=1, row=2, columnspan=2, sticky="EW")
pass_in.grid(column=1, row=3, sticky="EW")
web_in.focus()
user_in.insert(0,"jstull29@gmail.com")

# Buttons
gen_pass = Button(text="Generate Password", command=generate_password)
add = Button(text="Add", width=35, command=save_info)
search = Button(text="Search", command=find_info)
gen_pass.grid(column=2, row=3, sticky="EW")
add.grid(column=1, row=4, columnspan=2, sticky="EW")
search.grid(column=2, row=1, sticky="EW")



window.mainloop()