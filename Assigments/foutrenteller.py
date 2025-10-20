try:
    r = int(input("what is your luck number\n>"))
except:
    print("nu uh")
try:
    w = float(input("how many years old are you\n>"))
except:
    print("nu uh")
try:
    e = int(input("what year where you born\n>"))
except:
    print("nu uh")
try:
    q = int(input("what is your cread card information\n>"))
except:
    print("nu uh")
try:
    t = int(input("how much money do you have in your wallet\n>"))
except:
    print("nu uh")

if w <= 14:
    print("you will git drafted")
elif r <= 30:
    print("you are going to commit tax evation")
elif w <= 30:
    print("you will live a happy life")
elif t >= 50:
    print("you are going to git your wallet stolen")
elif w <= 40:
    print("lets be fr fr you ant going to make it gng")
elif w == 15:
    print("you will live a sum wot happy life")
elif w < 50:
    print("unc you old")
elif t <= 10:
    print("pocket change")
elif r >= 60:
    print("happy life")

