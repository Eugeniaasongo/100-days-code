print( "MY LOGIN SYSTEM")
print("+++++++++++++++")
username = input("Username >")
password = input("Password >")
if username == "Daniel" and password == "pas":
    print("Welcome " + username + "! you have been logged in!")
elif username =="David" and password == "totallyNotBald":
    print("Why hello there David, what a lovely accent you have,"
          "you could have charmed your way in here even without a password")
    print("Have a great day!")
    print("Don't forget to wear a hat in the sun!")
elif username == "Eugenia" and password == "boldy":
    print("Welcome " + username + "! you have a nice name")
else:
    print("Go away")

