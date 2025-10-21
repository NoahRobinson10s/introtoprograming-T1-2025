#petrograd russia march 8 1917 you walk to your home and you see a crowed of angey 
#as you walk home you see people then more people then a crowed they where protesting the tsar
#then you walk home and go to bed.
#the next morning you hear from your nabor that a revolution has started worred for your family you decide to head back to tsaritsyn where you family is.
#you decide to take the train to moscow and take a horse to tsaritsyen.
#you walk to the train station and you see a crowd looking like 
#outside the train station you see after that you head inside the train station.
#this story is not historcly accuret and in not ment to be.it is just a story.
#you head to the train station to get to a train to moscow when you get to the train station you see [noun 3]
#and you keep walking and bord the train and sit down on a 
#as you leave petrograd you nod off and fall into slumber
#you awake and leave the train after it arives to the station.
#after you get of the train you walkout of the station then you go to a horse stable a buy a horse
#you decicde to name the hourse [noun 5]
#soune you leave moscow to head to tsaritsyn and your first stop is ryazan.
#it took one day 1 to arive to ryazan entering the city you buy some 
#and leave the city
#you head for the city of tsaritsyn and so you keep moveing and after near 6 days you arive to tsaritsyn.
#you head for your house and open the door you see your family and move inside you pick up a [noun 7]
#you soon hear about the revalution and ensure your famialy that it will be all okay.
#sone you eat a hot bowl of  and go to bead on and you think about your familys safty and you drift of into slumber.
print("yur cahricter is noverosk yepskinskiy pronounced no-ver-osk yep-skins-kiy you live in petrograd russia in 1917 (that is pre USSR)")
print("petrograd russia march 8 1917 you walk to your home and you see a crowed of angey as you walk home you see people then more people then a crowed they where protesting the tsar")
def first():
    print("do you")
    print("1.go twords the yelling")
    print("2.you go home")
    choose = input(">")
    if choose == "1":
        yelling()
    elif choose == "2":
        go_home()
    else:
        print("invaled input")
        first()

def yelling():
    print("you go twords the crowed they are protesting the tsar and you join the protest after a day of protesting you go home")
    two()

def go_home():
    print("as you walk home you see people then more people then a crowed they where protesting the tsar then you walk home and go to bed.the next morning you hear from your nabor that a revolution has started you worrey for your familly in tsaritsyn")
    two()

def two():
    print("do you")
    print("1.go take a train to moscow")
    print("2.take your horse and ride to tsaritsyn")
    print("3.you dont go to tsaritsyn")
    choose = input(">")
    if choose == "1":
        train()
    elif choose == "2":
        horse()
    elif choose == "3":
        stay()
    else:
        print("invaled input")
        two()

    def train():
        print("you decide to take the train to moscow.you walk to the train station and you see a crowd looking like a mob outside the train station after that you head inside the train station and bord the train and sit down on a as you leave petrograd you nod off and fall into slumber you awake and leave the train after it arives to the station.after you get of the train you walkout of the station then you go to a horse stable a buy a horse")
        nameing_house = input("name the horse")

first()
   