import tkinter as tk
from tkinter import messagebox
from sql_database import append_user 
from registration import register_user_page


def naya_user():
    username = entry_username.get()
    password = entry_naya_user_password.get()

    if append_user(username,password):
        messagebox.showinfo("Success","Login Successful")
        entry_username.delete(0, tk.END)
        entry_username.delete(0, tk.END)
    else: 
        messagebox.showinfo("Error,Invalid username or password.")

root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="Maroon") 

tk.Label(root,text="Username:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root,text="Password:").pack()
entry_naya_user_password = tk.Entry(root,show="*")
entry_naya_user_password.pack()


tk.Button(root, text="Login", command=naya_user).pack(pady=5)
tk.Button(root, text="Register", command=register_user_page).pack(pady=5)
root.mainloop()