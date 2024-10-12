from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    epassword.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list.extend([random.choice(symbols) for char in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for char in range(nr_numbers)])
    random.shuffle(password_list)

    password = "".join(password_list)
    epassword.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = ewebsite.get()
    user = euser.get()
    password = epassword.get()
    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }
    if website=="" or user=="" or password=="":
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open (file="password_manager_start/data.json", mode='r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open(file="password_manager_start/data.json", mode='w') as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open(file="password_manager_start/data.json", mode='w') as f:
                    json.dump(data, f, indent=4)
            finally:
                ewebsite.delete(0,END)
                epassword.delete(0,END)

# ----------------------------- SEARCH -------------------------------- #
def search():
    website = ewebsite.get()
    try:
        with open("password_manager_start/data.json","r") as f:
            data = json.load(f)
    except FileNotFoundError as error_message:
        messagebox.showerror(title="Error" , message="File not found error.")
    else:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="password_manager_start/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1,row=0)

lwebsite = Label(text="Website:")
lwebsite.grid(column=0, row=1)

luser = Label(text="Email/Username:")
luser.grid(column=0, row=2)

lpassword = Label(text="Password:")
lpassword.grid(column=0, row=3)

ewebsite = Entry(width=34)
ewebsite.grid(column=1, row=1)

euser = Entry(width=53)
euser.grid(column=1, row=2, columnspan=2)

epassword = Entry(width=34)
epassword.grid(column=1, row=3)

bgenerate = Button(text="Generate Password", command=generate_password, width=14)
bgenerate.grid(column=2, row=3)

badd = Button(text="Add", width=44, command=save_data)
badd.grid(column=1, row=4, columnspan=2)

bsearch = Button(text="Search", width=14, command=search)
bsearch.grid(column=2, row=1)

window.mainloop()