default_pass = "abbas10"
for i in range(10):
    password_input = input("please input your password: \n")
    if password_input == "":
        print("please input correct password")
        break
    else:
        if password_input == default_pass:
            print("you have been logged in")
            break