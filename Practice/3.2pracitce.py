number = 5
if number > 5:
    print("the number is positive")

number = -3
if number > 0:
    print("the number is positive")
else:
    print("the number is not positive")

a = 1 
b = 2
c =3
if True:
    print("if statment ran")

else:
    print("plum")

d = input("how do you spell tree\n>")
print(d == "tree")
if d == "tree":
    print("correct")
else:
    print("false")

password = input("what is your password\n>")
print(password == "salsa")
if password == "salsa":
    print("access accsepted")
else:
    print("nu uh gng wrong password access denied")

password = input("what is your password\n>")
print(password == "salsa")
def password_function():
    if password == "salsa":
        print("access accsepted")
    
    else:
        print("nu uh gng wrong password access denied")
    password_function()
password_function()
