from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
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

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password} \n")
                    web_in.delete(0, END)
                    pass_in.delete(0, END)
    

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
gen_pass = Button(text="Generate Password")
add = Button(text="Add", width=35, command=save_info)
gen_pass.grid(column=2, row=3, sticky="EW")
add.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()