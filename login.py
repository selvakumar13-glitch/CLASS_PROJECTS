username = "admin"
password = "1234"

print("===== LOGIN SYSTEM =====")

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("Login Successful!")
    print("Welcome", user)
else:
    print("Invalid Username or Password")