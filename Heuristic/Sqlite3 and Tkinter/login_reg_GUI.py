import tkinter
root = tkinter.Tk()
root.geometry('500x500')
root.configure(bg = 'magenta')

lbl = tkinter.Label(root,text="Enter Username",font=('Arial 18'))
lbl.place(x=160,y=20)
username = tkinter.Entry(root, textvariable= "uname",font=('Arial 18'))
username.place(x=120,y=80)

lbl2 = tkinter.Label(root,text="Enter Password",font=('Arial 18'))
lbl2.place(x=160,y=150)
password = tkinter.Entry(root, textvariable = "pass",font=('Arial 18'))
password.place(x=120,y=200)

btn  = tkinter.Button(root,font=("times new roman",14),text="Login",width=10,height=2,bg='royal blue')
btn.place(x=100,y=250)
btn  = tkinter.Button(root,font=("times new roman",14),text="Register",width=10,height=2,bg='royal blue')
btn.place(x=300,y=250)



root.mainloop()
