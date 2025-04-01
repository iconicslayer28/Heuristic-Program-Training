import tkinter as tk 
from tkinter import messagebox
from sql_database import append_user 

def register_user():
    username = entry_reg_username.get()
    password = entry_reg_password.get()

    if not username or not password:
        messagebox.showinfo("Error, All the fields must be field.")
        return 
    
    if append_user(username,password):
        messagebox.showinfo("Success, Registration successful.")
        entry_reg_username.delete(0,tk.END)
        entry_reg_password.delete(0,tk.END)
        root.destroy()
    else:
        messagebox.showinfo("Error, Fields must be field.")

def register_user_page():
    global root, entry_reg_username, entry_reg_password
    root = tk.Tk()
    root.title("Registration Page")
    root.geometry("400x300")
    root.configure(bg="maroon")

    tk.Label(root, text="username").pack()
    entry_reg_username = tk.Entry(root)
    entry_reg_username.pack()

    tk.Label(root, text="password").pack()
    entry_reg_password = tk.Entry(root, show="*")
    entry_reg_password.pack()

    tk.Button(root, text= "Register", command = register_user).pack()

    root.mainloop()
