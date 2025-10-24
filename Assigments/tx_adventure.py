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
    print("2.wait for your family to come to you")
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
        nameing_house = input("name the horse\n>")
        print("you also buy some bread and mayby some potato")
        print("do you go buy fruits")
        print("y or n")
        choose = input(">")
        if choose == "y":
            fruit()
        else:
            no_fruit()

def no_fruit():
    print(f"you buy no fruit and live the city after travelling for many days you are traped in a snow storm and running low on food but your percecltlly healthy hourse {nameing_houres} siting right there")
    print("do you eat your hourse")
    print("y or n")
    choose = input(">")
    if choose == "y":
        eat()
    else:
        no_eat()

def eat():
    print("you eat your hourse but you still die of hunger")

def no_eat():
    print("you survive the snow storm becuse you find a food storage cash buried in the snow and you eventully arive at tsaritsyn you quickly head to your familys home and open the door to see your wife and children as you walk in you find that they are all safe and happy you breaf a sigh of relife and smile")

def fruit():
    print("you buy some potatos and leave moscow as you travile along you discover a nagat revolver you pick it up and ride to ryazan as you enter the city and pass through with out troble you keep riding and eventully arive at tsaritsyn you quickly head to your familys home and open the door to see your wife and children as you walk in you find that they are all safe and happy you breaf a sigh of relife and smile")

def stay():
    print("you decide to stay in petrograd not whaning to risk being killed by bandits day after day you whte and wate and do your work dillgently you hear that the bolsiviks had captured many cities including tsaritsyen after hearing of the great sovit milltary you join hopeing to protect your family form perscution and hopeing to find your self in a good position after the war as a mittary vet yourself you are immedatlly acceptid into the army and are sent to the front lines of war it is now febuyary 1919 and you are shiped off to tsaritsyn the city where your family lives as you arrive you hear of a inpending attak by the white russians and in the morning it comencis the ground sakes as artilly sells hit the ground")
    print("what do you do")
    print("1.run away")
    print("2.fight")
    choose = input(">")
    if choose == "1":
        run()
    elif choose == "2":
        fight()
    else:
        print("invaled input")
        two()

def run():
    print("")

def fight():
    print("you fight and fight for hours one after another the enemy shoot at you after hours of that they stop and retreat you cheer an yell but it it is a cruil reminder of what is to come after months of constant artillry barages and attacks the enemy breacks through and you rettreat during your retreat you see your commanding offacer shoot fellow sogers after that you decide to flee the red army and deffect to the white russians.you take your family and flee over the volga river and after days of rideing on horse back you arrive at omsk and leave your family there and sign up to the white russian army it is now may 1919 you are shiped off to help some amercians fight in the war where you meet dom you and dom grew into battale brothers he talks about his life in a place called micagen.after about a mounth of fighting with them they leave after 2 more years of fighting the white russians are essantally deffited and you flee to france but you hate french people and you rember doms words that if the war ever went soulth you and your family could go to micgen and he wode help you get on your feet so you and your family go to amercia and end up in detroit micgan and settal down in a small town building a new life in the land of oppertunity but you still remember your time in the war every thunderstrom and every fire work that is lit off.")
    print("ending:AMERCIAN DREAM ENDING")

def horse():
    print("you what for your family to come to petrograd after 3 weeks of waiting they arive and you settle in for a long summer you hear of blosivk recrutmant do you want to join")
    print("what do you do")
    print("1.join the red army")
    print("2.dont join the read army")
    choose = input(">")
    if choose == "1":
        join()
    elif choose == "2":
        stay_with_family()
    else:
        print("invaled input")
        two()

def join():
    print("you fight and fight for hours one after another the enemy shoot at you after hours of that they stop and retreat you cheer an yell but it it is a cruil reminder of what is to come after months of constant artillry barages and attacks the enemy breacks through and you rettreat during your retreat you see your commanding offacer shoot fellow sogers after that you decide to flee the red army and deffect to the white russians.you take your family and flee over the volga river and after days of rideing on horse back you arrive at omsk and leave your family there and sign up to the white russian army it is now may 1919 you are shiped off to help some amercians fight in the war where you meet dom you and dom grew into battale brothers he talks about his life in a place called micagen.after about a mounth of fighting with them they leave after 2 more years of fighting the white russians are essantally deffited and you flee to france but you hate french people and you rember doms words that if the war ever went soulth you and your family could go to micgen and he wode help you get on your feet so you and your family go to amercia and end up in detroit micgan and settal down in a small town building a new life in the land of oppertunity but you still remember your time in the war every thunderstrom and every fire work that is lit off.")
    print("ending:AMERCIAN DREAM ENDING")

def stay_with_family():
    print("you stay with your family and after many days and months of unrest and violance you decide to go to your orignal home in Helsinki finland your wife protests")
    print("do you lisen to your wife")
    print("1.you do")
    print("2.you dont")
    choose = input(">")
    if choose == "1":
        lisen()
    elif choose == "2":
        you_dont_lisen()
    else:
        print("invaled input")
        two()
def lisen():
    print("")

def you_dont_lisen():
    print("you dissigry with your wife and decide to go to Helsinki you ready your hourse named")
    hourse_name = input("give your hourse a name\n>")
    print("you leave petrograd and head to Helsinki")

first()