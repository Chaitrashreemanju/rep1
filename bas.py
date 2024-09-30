# VALIDATE USERNAME AND PASSWORD 
actual_username=input("enter:")
actual_password=input("enter:")
while True:
    username=input("enter the username:")
    if username==actual_username:
        break
for _ in range(3):
    password=input("enter the password:")
    if password==actual_password:
        break
else:
    print("User Blocked")                


                    
        