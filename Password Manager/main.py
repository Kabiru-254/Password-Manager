from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


def search():
    website_search = website_input.get()
    try:
        with open("data.json", mode="r") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No data file found!")
    else:
        if website_search in data:
            email_search = data[website_search]["email"]
            password_search = data[website_search]["password"]
            pyperclip.copy(password_search)
            messagebox.showinfo(title=website_search, message=f"The email is: {email_search}\nThe password is:"
                                                              f" {password_search}\nPassword copied!")
        else:
            messagebox.showerror(title="Error!", message=f"Sorry! No details for {website_search} exist!")

        # ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = username_input.get()
    user_password = password_input.get()

    new_dict = {
        website: {
            "email": email,
            "password": user_password
        }
    }

    if len(website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops!", message="Please fill in all the fields!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                old_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_dict, data_file, indent=4)
                messagebox.showinfo(title="Success!", message="Details added successfully!")
        else:
            with open("data.json", mode="w") as file:
                old_data.update(new_dict)
                json.dump(old_data, file, indent=4)
                messagebox.showinfo(title="Success!", message="Details added successfully!")
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(highlightthickness=0, height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2, columnspan=2)

website_label = Label(text="Website: ")
website_label.grid(row=2, column=1)

email_label = Label(text="Email/Username: ")
email_label.grid(row=3, column=1)

password_label = Label(text="Password: ")
password_label.grid(column=1, row=4)

website_input = Entry(width=36, fg="blue")
website_input.grid(row=2, column=2)
website_input.focus()

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=2, column=3)

username_input = Entry(width=55, fg="blue")
username_input.grid(row=3, columnspan=2, column=2)
username_input.insert(0, "shakazulu.shkz@gmail.com")

password_input = Entry(fg="blue", width=36)
password_input.grid(row=4, column=2)

generate_button = Button(text="Generate password", width=15, command=generate)
generate_button.grid(row=4, column=3)

add_button = Button(text="Add Password", width=47, command=save)
add_button.grid(row=5, column=2, columnspan=2)

window.mainloop()
