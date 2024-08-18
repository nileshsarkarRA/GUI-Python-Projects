## GUI Python Password Manager using Tkinter

import tkinter as tk
from tkinter import messagebox


def add_password():
    # accepting input from the user
    username = entryName.get()
    # accepting password input from the user
    password = entryPassword.get()
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added !!")
    else:
        messagebox.showerror("Error", "Please enter both the fields")


def get_password():
    # accepting input from the user
    username = entryName.get()

    # creating a dictionary to store the data in the form of key-value pairs
    passwords = {}
    try:
        # opening the text file
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                # creating the key-value pair of username and password.
                passwords[i[0]] = i[1]
    except:
        # displaying the error message
        print("ERROR !!")

    if passwords:
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        else:
            mess += "No Such Username Exists !!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST!!")


def get_list():
    # creating a dictionary
    passwords = {}

    # adding a try block, this will catch errors such as an empty file or others
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("No passwords found!!")

    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            # generating a proper message
            mess += f"Password for {name} is {password}\n"
        # Showing the message
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "Empty List !!")


def delete_password():
    # Prompting input from the user
    username = entryName.get()

    # creating a temporary list to store the data
    temp_passwords = []

    # reading data from the file and excluding the specified username
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")

        # writing the modified data back to the file
        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(line)

        messagebox.showinfo(
            "Success", f"User {username} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting {username}: {e}")


if __name__ == "__main__":
    password_manager_app = tk.Tk()
    password_manager_app.geometry("360x200")
    password_manager_app.title("Password Manager GUI by Nilesh")

    # Username customizations
    labelName = tk.Label(password_manager_app, text="Username")
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = tk.Entry(password_manager_app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    # Password Customizations 
    labelPassword = tk.Label(password_manager_app, text="Password")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = tk.Entry(password_manager_app)
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    # Add button
    buttonAdd = tk.Button(password_manager_app, text="Add Data", command=add_password)
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

    # Get button
    buttonGet = tk.Button(password_manager_app, text="Get Data", command=get_password)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    # List Button
    buttonList = tk.Button(password_manager_app, text="List all Data", command=get_list)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tk.Button(password_manager_app, text="Delete Data", command=delete_password)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

    password_manager_app.mainloop()