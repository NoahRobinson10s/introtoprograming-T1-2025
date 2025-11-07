import random
x = random.randint(1,101)
z = False
while z == False:
    y = int(input("put in number\n>"))
    if y > x:
        print("too high")
        z = True
    elif y < x:
        print("too low")
        z = True
    elif y == x:
        print("correct")
        z = True
    else:
        print("wrong awnser")
        z = False
