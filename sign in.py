from tkinter import *
def login():
  username = username_entry.get()
  password = password_entry.get()

  if username == "admin" and password == "password":
    message_label.config(text="Login Successful!")
  else:
    message_label.config(text="Invalid Username or Password.")


root = Tk()
root.title("Login Form")

# Username Label and Entry
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

# Password Label and Entry
password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# Login Button
login_button = Button(root, text="Login", command=login)
login_button.pack()

# Message Label
message_label = Label(root, text="")
message_label.pack()


root.mainloop()
