print("""
****************************
User Login Program
****************************
""")
sys_user_name="name"
sys_password="12345"
right_entry=3
while True:
    user_name=input("User Name:")
    password=input("Password=")
    if(user_name != sys_user_name and password == sys_password):
        print("Username is uncorrect...")
        right_entry -=1
    elif (user_name == sys_user_name and password != sys_password):
        print("Password is uncorrect...")
        right_entry -=1
        a=input("Click 5 if you forgot your password:")
        if(a == "5"):
            print("Password:12345")
            break
    elif(user_name != sys_user_name and password != sys_password):
        print("Username and password are uncorrect...")
        right_entry -=1
    else:
        print("Successfully logged into the system...")
        break
    if(right_entry == 0):
        print("Your right to login is over...")
        break
