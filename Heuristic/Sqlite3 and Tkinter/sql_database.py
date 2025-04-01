import sqlite3
conn = sqlite3.connect('')
print("Opened databses successfully.")

conn.execute('''CREATE TABLE Login_user 
             (ID No NOT NULL,
             Username NOT NULL,
             passkey NOT NULL)''')
print("Opened table successful.")

databases = {"username_id": [] ,"pasword_id":[]}

def append_user(username,password):
    databases["username_id"].append(username)
    databases["password_id"].append(password)

def verify_user(username,password):
    if username == "username_id":
        return True
    elif password == "password_id":
        print("Login Successful.")
conn.commit()
print("Records Saved Successfully.")
conn.close()
