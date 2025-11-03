king_activate = False
op_tower = 3000
my_tower = 3000
doubt = 0
def start():
    print("\nWhat game mode do you want to play?")
    print("1. Trophy Road")
    print("2. Classic 2v2")
    print("3. Neither, play Clash of Clans")
    print("4. Don't play a game and focus on your classwork.")
    choice = input(">>>")
    print()
    if choice == "1":
        first_play()
    elif choice == "2":
        print("You try to play a 2v2, but the server for 2v2s seems to be down. It's as if the creators of the game, while wanting to, didn't have the time or energy to make a whole different game mode. You play a trophy road game instead.\n")
        first_play()
    elif choice == "3":
        ending_1()
    elif choice == "4":
        classwork()
    else:
        print("Invalid Input. Must be a number 1-4.")
        start()
def first_play():
    print("You load into a trophy road game. Your opponent's tower level is two above yours and he's already spamming the pig shaking its butt emote.\n")
    print("The first 10 seconds pass and no one has played a card. You are leaking elixir, as is the enemy. What do you do?")
    print("1. Push Valkyrie and Prince on the bridge")
    print("2. Fireball the Towers")
    print("3. Split Skarmy in the back")
    print("4. Wait for the opponent to play first")
    choice = input(">>>")
    print()
    if choice == "1":
        prince_valk()
    elif choice == "2":
        cinema()
        fireball()
    elif choice == "3":
        split_skarmy()
    elif choice == "4":
        start_wait()
    else:
        print("Invalid Input. Must be a number 1-4.")
        first_play()
def prince_valk():
    global op_tower
    op_tower = op_tower - 500
    print("You push a Valk and Prince on the bridge. Your opponent plays a Pekka, which mostly defends, but you get a few hundred damage on the tower.\n")
    print("Your opponent is being a little coward and still not playing any offense. What do you do?")
    print("1. Fireball the Towers")
    print("2. Play Log to cycle")
    print("3. Place Baby Dragon in the back")
    print("4. Wait for your opponent to stop being a little baby while you spam chicken emotes")
    choice = input(">>>")
    print()
    if choice == "1":
        cinema()
        fireball()
    elif choice == "2":
        log_cycle()
    elif choice == "3":
        baby_dragon()
    elif choice == "4":
        print("You spam chicken emotes and wait for your opponent to place something.")
        mega_knight()
    else:
        print("Invalid Input. Must be a number 1-4.")
        prince_valk()
def split_skarmy():
    global op_tower
    global my_tower
    op_tower = op_tower - 100
    print("\nYour opponent feels no need to defend, and you get about a hundred damage on the tower.")
    print("\nYour opponent plays lumberjack and a balloon. How do you defend?")
    print("1. Fireball and Baby Dragon")
    print("2. Cannon and Inferno Dragon")
    print("3. Valkyrie and Freeze")
    choice = input(">>>")
    print()
    if choice == "1":
        print("The fireball does next to nothing to either card, and baby dragon doesn't help very much. Your tower takes a major hit.")
        my_tower = my_tower - 2500
        print("\nYou wasted a bunch of elixir on your useless defense, so you have to wait for your opponent to place something.")
        mega_knight()
    elif choice == "2":
        inferno_counter()
    elif choice == "3":
        print("Your valkyrie completely destroys the lumberjack, and the freeze allows the tower to take out some balloon health. The balloon still gets good damage in.\n")
        print("You spent a lot of elixir on defense, so you have to wait for your opponent to place something.")
        my_tower = my_tower - 750
        mega_knight()
    else:
        print("Invalid Input. Must be a number 1-4.")
        split_skarmy()
def start_wait():
    global my_tower
    print("Your opponent plays a Sparky on the bridge. What do you do?")
    print("1. Play Skarmy")
    print("2. Play Cannon")
    print("3. Play Valkyrie")
    print("4. Play Prince")
    choice = input(">>>")
    print()
    if choice == "1":
        print("The skarmy surround the sparky, and it is unable to attack all of them at once. The sparky is pacified quickly.")
        sparky_counterpush()
    elif choice == "2":
        print("The cannon is destroyed by the first sparky shot and the sparky gets multiple hits on the tower.")
        my_tower = my_tower - 1000
        emote_war()
    elif choice == "3":
        print("The valkyrie tanks the first hit, but doesn't kill it in time for the second hit. The Sparky gets a hit on the tower.")
        my_tower - my_tower - 500
        emote_war()
    elif choice == "4":
        print("The prince tanks the sparky his and takes it out in time.")
        sparky_counterpush()
    else:
        print("Invalid Input. Must be a number 1-4.")
        start_wait()
def fireball():
    global king_activate
    global op_tower
    king_activate = True
    op_tower = op_tower - 150
    print("You strategically place your fireball to hit the King and Princess tower. You're a genius.\n")
    mega_knight()
def log_cycle():
    global op_tower
    print("\nYou play the log to cycle your cards. What do you do?")
    print("1. Fireball the Towers")
    print("2. Push with Inferno Dragon")
    print("3. Play Baby Dragon in the back")
    print("4. Wait for your opponent to place something")
    choice = input(">>>")
    print()
    if choice == "1":
        cinema()
        fireball()
    elif choice == "2":
        if king_activate == True:
            print("It would've worked, but you activated the King Tower by fireballing it so you only get chip damage.")
            op_tower = op_tower - 500
            print(op_tower)
            minute_left()
        else:
            print("Your opponent can't defend the dragon and you get a lot of damage on the tower.")
            op_tower = op_tower - 2000
            minute_left()
    elif choice == "3":
        baby_dragon()
    elif choice == "4":
        mega_knight()
    else:
        print("Invalid Input. Must be a number 1-3.")
        log_cycle()
def baby_dragon():
    global op_tower
    print("\nWhat do you back the Baby Dragon up with?")
    print("1. Inferno Dragon")
    print("2. Prince")
    print("3. Nothing, let it alone")
    choice = input(">>>")
    print()
    if choice == "1":
        print("Your opponent uses a rocket and destroys your push.")
        minute_left()
    elif choice == "2":
        print("Your opponent tries to defend Prince with a skarmy, but the baby dragon takes it out quickly and you get good tower damage.")
        op_tower = op_tower - 2500
        minute_left()
    elif choice == "3":
        print("The Baby Dragon does next to no damage on its own.")
        op_tower = op_tower - 200
        minute_left()
    else:
        print("Invalid Input. Must be a number 1-3.")
        baby_dragon()
def mega_knight():
    print("\nYour opponent sends a laughing emote and places a Mega Knight. What do you do?")
    print("1. Place a cannon to distract")
    print("2. Play Inferno Dragon on the Mega Knight")
    print("3. Push Skarmy on the other lane")
    print("4. Accept Defeat")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You place a cannon to distract the Mega Knight.")
        mk_cannon()
    elif choice == "2":
        mk_inferno()
    elif choice == "3":
        mk_skarmy()
    elif choice == "4":
        global doubt
        doubt = doubt + 1
        print("No you don't. You must keep playing. This is why we Clash. You place a cannon to distract the Mega Knight.")
        mk_cannon()
    else:
        print("Invalid Input. Must be a number 1-3.")
        mega_knight()
def inferno_counter():
    global op_tower
    global my_tower
    print("The cannon distracts both cards long enough for your inferno dragon to mostly defend, but your tower still takes damage. The Inferno Dragon gives you a counterpush.")
    print("\nWhat do you back it up with?")
    print("1. Baby Dragon")
    print("2. Prince")
    print("3. Freezing the tower")
    choice = input(">>>")
    print()
    if choice == "1":
        print("Your opponent tries to distract with a skarmy, but the baby dragon easily takes them out. You get good damage on the tower.\n")
        op_tower = op_tower - 2000
        minute_left()
    elif choice == "2":
        print("Your opponent places a skarmy and easily counters.\n")
        minute_left()
    elif choice == "3":
        print("Your opponent distracts the inferno dragon with a skarmy, and then the skarmy gets chip damage on your tower.")
        my_tower= my_tower - 200
        minute_left()
    else:
        print("Invalid Input. Must be a number 1-3.")
        inferno_counter()
def sparky_counterpush():
    global op_tower
    print("\nHow do you counter-push?")
    print("1. Inferno Dragon")
    print("2. Skarmy")
    print("3. Baby Dragon")
    print("4. Valkyrie")
    choice = input(">>>")
    print()
    if choice == "1":
        print("Your opponent places a bulding to late and the Inferno Dragon locks onto the tower. You get good damage in.\n")
        op_tower = op_tower - 1000
        mega_knight()
    elif choice == "2":
        print("Your opponent counters it easily with a log.\n")
        mega_knight()
    elif choice == "3":
        print("Your opponent plays an executioner and easily counters it.\n")
        mega_knight()
    elif choice == "4":
        print("Your opponent plays skarmy on the valkyrie for some reason and you get easy damage on the tower.\n")
        mega_knight()
        op_tower = op_tower - 500
    else:
        print("Invalid Input. Must be a number 1-4.")
        sparky_counterpush()
def emote_war():
    print("\nYour opponent sends a laughing emote, very proud of what one of the most no-skill cards in the game did. How do you counter?")
    print("1. Chicken emote")
    print("2. Pig shaking its butt emote")
    print("3. Goblin mimimimi emote")
    print("4. Goblin rolling eyes emote")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You get ragebaited successfully and you were distracted long enough for your opponent to place a sneaky golem and take your tower.")
        if doubt > 0:
            ending_2()
        else:
            ending_3()
    elif choice == "2":
        emote_war_2()
    elif choice == "3":
        print("You prove that you're a pay to win because you spent 5 dollars on an emote. Your opinion is invalidated. The match continues.\n")
        minute_left()
    elif choice == "4":
        emote_war_2()
    else:
        print("Invalid Input. Must be a number 1-4.")
        emote_war()
def emote_war_2():
    print("\nYou counter his emote, but then he sends a baby crying emote. What do you send back?")
    print("1. Shrugging emote")
    print("2. Goblin mimimimi emote")
    print("3. Mute him")
    print("4. Do nothing and focus on the game")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You counter successfully and your opponent leaves out of shame. This is what the internet has come to. You get an easy 3-crown.")
        ending_5()
    elif choice == "2":
        print("You prove that you're a pay to win because you spent 5 dollars on an emote. Your opinion is invalidated. The match continues.\n")
        minute_left()
    elif choice == "3":
        print("You mute him. He is too distracted spamming emotes, so you send a single skarmy and it takes his tower.")
        if doubt > 0:
            ending_4()
        else:
            ending_5()
    elif choice == "4":
        print("You won spiritually, but this is online, that doesn't exist. Your opponent pulls out a push I can't even say out loud. All I can say is you're doomed.")
        ending_2()
    else:
        print("Invalid Input. Must be a number 1-4.")
        emote_war_2()
def mk_cannon():
    global my_tower
    global op_tower
    my_tower = my_tower - 500
    print("\nThe cannon distracts the Mega Knight long enough for the tower to only take a few hits. You suspect the opponent has no elixir. What do you do?")
    print("1. Push with Inferno Dragon")
    print("2. Push with Skarmy")
    print("3. Push with Prince")
    print("4. Wait to build more elixir before pushing.")
    choice = input(">>>")
    print()
    if choice == "1":
        if king_activate == True:
            print("It would've worked, but you activated the King Tower by fireballing it so you only get chip damage.")
            op_tower = op_tower - 500
            print(op_tower)
            minute_left()
        else:
            print("Your opponent can't defend the dragon and you get a lot of damage on the tower.")
            op_tower = op_tower - 2000
            minute_left()
    elif choice == "2":
        print("He didn't have a lot of elixir, but he had a little. Your push gets ruined by a single log.\n")
        minute_left()
    elif choice == "3":
        prince_push()
    elif choice == "4":
        tower_rocket()
    else:
        print("Invalid Input. Must be a number 1-4.")
        mk_cannon()
def mk_inferno():
    global my_tower
    my_tower = my_tower - 500
    print("The dragon kills the Mega Knight in a decently short time, but there was nothing distracting it, so it gets a few hits on the tower.\n")
    print("Mega Knight costs 7 elixir, so you should be able to play something.")
    print("1. Push with Prince")
    print("2. Push with Skarmy")
    print("3. Wait to build elixir")
    choice = input(">>>")
    print()
    if choice == "1":
        prince_push()
    elif choice == "2":
        print("He didn't have a lot of elixir, but he had a little. Your push gets ruined by a single log.\n")
        minute_left()
    elif choice == "3":
        tower_rocket()
    else:
        print("Invalid Input. Must be a number 1-3.")
        mk_inferno()
def mk_skarmy():
    global my_tower
    my_tower = my_tower - 2500
    global op_tower
    op_tower = op_tower - 2
    print("Why? You get like 2 damage on the opponents tower, and he gets 2500 on yours.\n")
    print("What do you do now?")
    print("1. Push with Inferno Dragon")
    print("2. Push with Prince")
    print("3. Spam the 6 7 emote and do nothing else.")
    choice = input(">>>")
    print()
    if choice == "1":
        if king_activate == True:
            print("It would've worked, but you activated the King Tower by fireballing it so you only get chip damage.")
            op_tower = op_tower - 500
            minute_left()
        else:
            print("Your opponent can't defend the dragon and you get a lot of damage on the tower.")
            op_tower = op_tower - 2000
            minute_left()
    elif choice == "2":
        prince_push()
    elif choice == "3":
        ending_6()
    else:
        print("Invalid Input. Must be a number 1-4.")
        mk_skarmy()
def prince_push():
    global op_tower
    op_tower = op_tower - 2000
    global my_tower
    print("Prince is the best and most balanced card. Your opponent's tower takes massive damage.\n")
    print("Your opponent tries to get you back with a goblin barrel. You have almost no elixir. What do you do?")
    print("1. Play Log on the goblins")
    print("2. Let the tower take care of the goblins")
    choice = input(">>>")
    print()
    if choice == "1":
        print("The log takes the goblins out quickly. They get no damage on the tower.")
        minute_left()
    elif choice == "2":
        print("Your opponent freezes the tower and the goblins get a lot of damage.")
        my_tower = my_tower - 500
        minute_left()
    else:
        print("Invalid Input. Must be a number 1-2.")
        prince_push()
def tower_rocket():
    global my_tower
    global op_tower
    my_tower = my_tower - 600
    print("As you build more elixir, so does your opponent. He rockets your tower\n")
    print("Rocket costs 6 elixir, so he has to be low. What do you do?")
    print("1. Push with Baby Dragon")
    print("2. Push with skarmy")
    print("3. Fireball the towers")
    print("4. Wait for more elixir again")
    choice = input(">>>")
    print()
    if choice == "1":
        print("Your opponent can't defend, good play.")
        op_tower = op_tower - 1000
        minute_left()
    elif choice == "2":
        print("Your opponent plays log. Why do people have swarm decks?")
        minute_left()
    elif choice == "3":
        print("You know, you should save spells for when your opponent can actually defend, but okay.")
        op_tower = op_tower - 200
        minute_left()
    elif choice == "4":
        print("Your opponent mirrors rocket on the tower. Just play a card, you coward.")
        my_tower = my_tower - 600
        minute_left()
    else:
        print("Invalid Input. Must be a number 1-4.")
        tower_rocket()
def minute_left():
    global op_tower
    global doubt
    print("\nYou enter the last minute of the game, and 2x elixir activates. No towers have been taken yet. What do you do?")
    print("1. Push with Valkyrie and Prince")
    print("2. Spell the tower")
    print("3. Wait for your opponent to play first")
    print("4. Why play at all?")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You push Valkyrie and Prince. Your opponent can only stall with a tesla tower, and takes some good damage.")
        op_tower = op_tower - 500
        if op_tower <= 0 and doubt > 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_4()
        elif op_tower <= 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_5()
        else:
            final_play()
    elif choice == "2":
        print("You spell the tower. It gets a little damage.")
        op_tower = op_tower - 200
        if op_tower <= 0 and doubt > 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_4()
        elif op_tower <= 0:
            print("And that's all the damage you need to get the tower. Your opponent tries to spam on the bridge, but you defend enough to outlast the timer.")
            ending_5()
        else:
            final_play()
    elif choice == "3":
        print("You decide its better to wait for your opponent to plays first so you can properly counter.")
        final_wait()
    elif choice == "4":
        doubt = doubt + 1
        print("But think of the trophies. Think of the evolutions you'll unlock. You have some time to reflect on this while you wait for your opponent to play first.")
        final_wait()
    else:
        print("Invalid Input. Must be a number 1-4.")
        minute_left()
def final_wait():
    global my_tower
    global doubt
    print("\nAaaaaand he played a Mega Knight and a Pekka together somehow. How do you defend?")
    print("1. Skarmy")
    print("2. Cannon")
    print("3. Evo credit card")
    print("4. Surrender and spam emotes")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You place a skarmy behind the Pekka as a last desperate play. It somehow works and distracts both troops long enough to not take damage. Your opponent must be fuming.")
        final_play()
    elif choice == "2":
        print("You place a cannon to distract. It takes out the Mega Knight, but the Pekka still does massive damage to your tower")
        my_tower = my_tower - 2000
        if my_tower <= 0 and doubt > 0:
            print("The Pekka takes your tower and your opponent sends a chicken emote.\n")
            ending_2()
        elif my_tower <= 0:
            print("The Pekka takes your tower and your opponent sends a chicken emote.\n")
            ending_3()
        else:
            final_play()
    elif choice == "3":
        secret_ending_2()
    elif choice == "4":
        doubt = doubt + 1
        print("You can't give up when you came this far. You must keep pushing. You must reach 10k trophies or your life will have no meaning. You place a skarmy behind the Pekka and hope it works.\n\nIt somehow works and distracts both troops long enough to not take damage. Your opponent must be fuming.")
        final_play()
    else:
        print("Invalid Input. Must be a number 1-4.")
        final_wait()
def final_play():
    global op_tower
    global my_tower
    print("\nIt's overtime now. You feel like this game has lasted forever. If you lose this game, you might consider thinking about deleting the game. What do you do?")
    print("1. Push with Prince and Valkyrie")
    print("2. Push with Baby Dragon and Inferno Dragon")
    print("3. Push with Skarmy and freeze on the tower")
    print("4. Place skarmy in the back and cannon in the center for defense")
    if doubt == 3:
        print("-OR-")
        print("5. Delete Clash and end the pain")
    choice = input(">>>")
    print()
    if choice == "1":
        print("You play a strong push and the opponent is unable to defend.\n")
        op_tower = op_tower - 2000
        if op_tower <= 0 and doubt > 0:
            ending_4()
            return
        elif op_tower <= 0:
            ending_5()
            return
        else:
            print("But it's not enough. The tower is till hanging on by a thread and you are out of elixir. The opponent plays evo goblin barrel and freezes the tower.\n")
            if doubt > 0:
                ending_2()
                return
            else:
                ending_3()
                return
    elif choice == "2":
        print("You play a completely arial push. The opponent did not prepare for this and you ravage the tower.\n")
        if doubt > 0:
            ending_4()
            return
        else:
            ending_5()
            return
    elif choice == "3":
        print("Your opponent counters with a single log. You're done for. He plays evo goblin barrel and freezes the tower.")
        if doubt > 0:
            ending_2()
            return
        else:
            ending_3()
            return
    elif choice == "4":
        print("Your Opponent spams in one lane to get a quick win, but your defense tanks most of the damage.\n")
        my_tower = my_tower - 500
        if my_tower <= 0:
            print("But most doesn't cut it. That little bit of damage is all he needs.\n")
            if doubt > 0:
                ending_2()
                return
            else:
                ending_3()
                return
        else:
            print("Your opponent runs out of elixir and you are free to place one prince and take the tower.\n")
            if doubt > 0:
                ending_4()
                return
            else:
                ending_5()
                return
    elif choice == "5" and doubt == 3:
        secret_ending()
    else:
        if not doubt == 3:
            print("Invalid Input. Must be a number 1-4.")
        else:
            print("Invalid Input. Must be a number 1-5.")
        final_play()
def classwork():
    for i in range(1000):
        print()
    print("I will let you do work if you can actually tell me what class you're in.")
    print("1. English")
    print("2. Math")
    print("3. Science")
    print("4. History")
    choice = input(">>>")
    print()
    if choice == "1":
        print("Nope. You hop on clash play a trophy road game.")
        first_play()
    elif choice == "2":
        print("Nope. You hop on clash play a trophy road game.")
        first_play()
    elif choice == "3":
        print("Nope. You hop on clash play a trophy road game.")
        first_play()
    elif choice == "4":
        ending_7()
    else:
        print("No. Don't chicken out of the question.")
        classwork()
def ending_1():
    print("\nYou play Clash of Clans.")
    print("Ending 1 of 7: Worst Ending\n")
def ending_2():
    print("\nYour opponent spams the laughing emote as you have to watch yourself get 3-Crowned no diff. You will never psycologically recover from this game. Why DO we Clash?")
    print("Ending 2 of 7: Crashout\n")
def ending_3():
    print("\nYou let out a huge sigh as your opponent somehow edges out a win. But if you play ONE more game, you'll come back.")
    print("Ending 3 of 7: Denial\n")
def ending_4():
    print("\nYou won, but what does it matter? You will only lose a thousand more games. You would dwell on this thought, but you fingers already clicked the 'play again' button. Eh, one more game.")
    print("Ending 4 of 7: Doubt\n")
def ending_5():
    print("\nLOOOL GGS TOO EZ THIS IS THE BEST GAME EVER")
    print("Ending 5 of 7: Pride\n")
def ending_7():
    print("Wow. You actually got it. I guess you can focus on you classwork now.")
    print("Ending 7 of 7: Functional Human Being")
def secret_ending():
    print("\nYou decide that is enough screwing around with your life. You delete Clash and you invest in your future. You grow up to marry your soulmate and have 3 children who live with you in your mansion.")
    print("Secret Ending 1: Best Ending\n")
def ending_6():
    print("****###********####*+-::-*####*##%%%*#%%####**#%##%%%%%%%%#####*+:...:--==+*#=+#####*++**#%%@@@#%@@@")
    print("****#%%%@@@@@%#####%%*-+###%#**%%%%%#*%####%######%%%%%%%%%%####*+:=#@%***###%#%%#%@%###*#%@@##**#%#")
    print("***#%@@@@%@@%%%%@@@@%**#**##**####%%%##%#%##%#%%%#%%@%@%%%%%%#%##*=:+@%##%#####%#*%%%@#%%#*#@#%%%%%%")
    print("*##%@%@@%%%##%@@@@@%**#**##*###%#%@@@%#%#%##%#%%%#%%@%%%%##%%%#%##*=:-*##%#**#%%*#%#*%%%%%%%@@%#%@@%")
    print("*#%%%@@%%@##%@@@@@%**#**######%%%%@@@%##%%%%%%#%%###%%######%%#%%##*+:.+%%#+**%@%@#*#@*=%@@@@%*-*%%@")
    print("**%#%%###%%%@@@@@%**##**###%%%%%%@@@%#*%%%%%%%###%%#########%#%%###**+::#%*=+*##%%#%%#+*%@@%%%#+*%%@")
    print("*#%#%#**#%@%%%%%%+*##**#########%%%%##%%%@%%%%%%%%%%%%%%%%%%%%%%%%%#**+:-*#=-*#*###%@*-+%@%#*#***%%%")
    print("*###%#**#%%####%-*###**%#%%%%%%#####%%#%@@%%%%%%%@@@@@@@@@@@@@@%%%%%#**+::*#+*%#%#***+=*%###+#+--=*%")
    print("##%#%###%%%@@@@*+####*%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%%%@@@@@%%%###+-+**#@%##*%#+*##***%@#**##%")
    print("#%%%@%@@%%%*=+=-#####%%%%%%%%%########%%%%%%##%%%%%%%%###***##%%%@@%%%%##+-=*#@@#**%%*#*#***#%#####@")
    print("%@@@%@@@%%####=**###%%%@%%%##**++++***##%%%%###%%%%%##**====+*##%%@@@@%%%#+::*%%***###%%##%%#*+*##@@")
    print("@@%@@@@@%@@@%*=######%#%####**+=---==+*#####**##%%%%#*+:....-=*#%%@@@@@@%%#*-+%@%#+***##%%%@%***#@%@")
    print("@@%@@@@@%@@@%=**#%%%%%%@%%##*+-.....-=+**##****#%%%##*+:....-=+#%%%@@@@@@%%#*++%#%@%**+#@@@@@%**###%")
    print("@@%@@@@@@@@@%=##%%@@@@@@%%%#*+=....:-=+***##***###%##*+=-::-=+*##%%@@@@@@@%%#*=----=*#*#@@@@@%@%#*#%")
    print("@@%@@@%@@@@@#+#%%@@@@@@@%%##*++-:::-=+*********#######**++++**###%%%@@@@@@@%%#**=-*%@@@%%@@@@%#####%")
    print("@@%@@@@@@@@@++#%@@@@@@@@###***++=++++++*********#####*********###%%%@@@@@@@@@%##*++#%%%%%%%#***##%#%")
    print("@@%@%@@@@@@%+*%%@@@@@@@%##****+++++++*********###%#%###*******####%@@@@@@@@@@@%%#*+=:=*%%####**#%%%%")
    print("%@%%##%%##%%++%%@%@@@@@%#******+++********####%%%%%%%%%##**######%%@@@@@@@@@@@@%%##***#%%#*#%%%%%%%%")
    print("%@%%**+#**##*+#%%%@@@@@##******+****#####%%@%%%%@@@@%%%%%#######%%%@@@@@@@@@@@@%%%#****%%#*#%@%%%%##")
    print("@@%%#*=--=+**+*#%@@@@@@##********##%#**##%###%%%%%%%%%#%%%%%%%%%%%@@@@@@@@@@@@%#*+=++##@@%##%@@@%%%#")
    print("@@%@%#*=----=+#%%@@@@@@###***####%%#********#############%%%@@%%%@@@@@@@@@@@@@%%#**#%@@@@@@@%@@@@%%%")
    print("@@@@@%*==+***##%%@@@@@@%#######%%#***++++++++*****#####%%%%%%@@@@@@@@@@@@@@@@@%%####%@@@@@@@@@@@@@@@")
    print("%@@@@@%+-=**##%%%@@@@@@%####%%@%#***************######%%%%%@@@@@@@@@@@@@@@@@@%####%@@@@@@@@@@@@@@@%@")
    print("##@@@@@@%++**##%@@@@@@@@#%%%%@%#*#####*****=--:+=-+***####%@@@@@@@@@@@@@@@@@@@%#*#@@@@@@@@@@@@@@@@@@")
    print("#%@@@@%*=++**#%%@@@@@@@@%%%%%@%#%%%#**---:::::.:.::---*+*##%@@@@@@@@@@@@@@%%@%%###%@@@#%%%%@@@@@@@@%")
    print("%%%##*=-==+*#%%%@@@@@@@@@%%%%@%%@@%#+=::::........:+#*###%%%@@@@@@@@@@@@@@%%%%*##*%@@@*###*#######%@")
    print("#**##*--=+**#%%%%%@@@@@@@@%%%@%@@@%#####**********#**####%%%@@@@@@@@@@@@@@@%###=+*#@@#+#%%%##%%%%%@@")
    print("%%##**%#***####%@@@@@@@@@@@%%%%@@@%%####**********#######%%%@@@@@@@@@@@@@@@@%%%#+-+%@@@%%@@@@%%%%%@@")
    print("%####%@@@%#*##%%@@@@@@@@@@@@%%@%@@%%%####*********#######%%%@@@@@@@@@@@@@@@@@@%##*+*@%%++**%@@@%%@@@")
    print("#%@@@@%@@@@%#*#%%@@@@@@@@@@@%%%@@@@%%#####********#######%%%@@@@@@@@@@@@@@@@@@@%##**+#+-=*#@%@@%@@#%")
    print("@%%@@%%@@@%%%%###%@@@@@@@@@@@%#%%@@%%####**********#######%%@%@@@@@@@@@@@@@@@@@%%##**=:-=%@@@@@@###@")
    print("@@@@@%%@@@@@@@@@%*%%@@@@@@@@@@%#%%%%%%###************#####%%%%@@@@@@@@@@@@@@@@@%%%###*==@@@@@@@@#%@@")
    print("@@@@%%@@%@@@@@@@%+*#%%@@@@@@@@%##%%%%%##***************###%%%%@@@@@@@@@@@@@@@@@@@%%###*=#@@@@@@@@@@@")
    print("@@@@@@@#+=+%@@@*-+*##%%%%@@@@@@####%%%###*************#######@@@@@@@@@@@@@@@@@@@@@%%%%###%@@@@@@@@@@")
    print("@@@@@@#==--*@#-=+**##%%%%%%@@@@%####%%#%##***********######%%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@#@@@@@@@@")
    print("@@@@@@#=--+%@+=+***#%%%%%%%%@@@@#####%%%%##**********#######%@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%#@@@@@@@@")
    print("%@@@@@@@@@@@%=+**####%%%%%%%%@@@%#####%%%#####*****#########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%%@@@@@@@@@*-=***###%%%%%%%%%%@@@######%%#####***##*#######%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%###@@@@@*--+**#%##%%%%%%%%%%%%@@@#########################%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("##*===+=--=+***##%%%%%%%%%%%%%%%@@%#######################%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("##*+--::=+***#####%@@%%%%%%%%%%%%%%%#####################%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("#**=-:-=+***##%%%#%%%@@%%%%%%%%%%%%%%###################%@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@")
    print("#**=::=***#####%%%%%%%@@@@%%%%%%%%%@%%###%%###########%%@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@")
    print("%**=:-=***####%%%%%%%%%@@@@@@@%%%%%@%@%###%%%#%####%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@")
    print("@#*=-=+**#######%%%%%%%%@@@@@@@@@@@@@@@%#%%%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@")
    print("@%*=-+**######%%%%%@%%%%%%@@@%%@@@@@@@@@%#%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@")
    print("@%+==**#######%%%%@@@%%%%%%@@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@")
    print("%#*=+*#####%%%%%%%%@@@%%%%%%@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@")
    print("%#*=*######%%%%%%%%%@@@@%%%%%%@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@")
    print("%#*+*####%%%%%%%%%%%@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%#*+*#####%%%%%@%%%%@@@@@@@%%@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    print("Siiix Seeeveeeeen. That's a real emote you can get in the game now.")
    print("Ending 6 of 7: 6 7\n")
def secret_ending_2():
    print("%%%%%%@@@@@@@@@@%%%%%%%%%%%#############*##########%%#%%%%%%%%%%#############################*###%%%%%%%%%%%%%%%#*********##################%%%%%%%%%%")
    print("%%%%%%%%@@@@@%%%%%%%%%%%#####********######**************************************************************************************#############%@@%%%%%")
    print("%%%%%%%%%%@%%%%%%%%%%%%###******###*++++++##+*+++++++++++++++++++++++++++++++++++++++++++++++*********++++**++****++++++***********#############%%%%%%")
    print("%%%%%%%%%@@%%%%%%%%%%###*****##*++++++++++*%##############################%######################################%%%%%%%%%%%%##*+***#############%%@%%")
    print("%%%%%%%@@@@@@%%%%%%%####***##*++++++++++++*#####################**#**##**########*##########################*****######*#%@@%%%%*+**###############%@%")
    print("%%%%%@@@@@@@@@@%%%%###***##++++***+++====++*#.                   .=---::...       .::                                      .*@%%%*****###############%")
    print("%%@@@@@@@@@@@@@@%%%##***#*+*+-:.....:-*===+*#+.  ....::-:. .  ..:-=----:::... ..::::.                                        -%@%#****########**###%%%")
    print("%@@@@@@@@@@@@@@@@@%##*#**++*.         =+-=++*#: .:-===*+:....:===-===----::..::---:.            ........................ ..   =@@%#****##########%%@%%")
    print("@@@@@@@@@@@@@@@@@@@%##*+*+#=   .*#=   .*--=++#*==-=*%#+-=::=-:::-:====------:-====: ..........................................-@@@#+***#####**#%%%%%@@")
    print("@@@@@@@@@@@@@@@@@@@%##*+++#:   .--.   .+--=++*#+-+@@*++=:=::::::::-=+===-==---===- ...........................................-@%%#*****#####%@@%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%#*++**#:          .+===+++#+-#@#*+==-::.:...::--++++===+=---=: ...........................................-@%%#****####%@%%@@%%%%%")
    print("@@@@@@@@@@@@@@@@@@@##***+*#%%#**++:   .+==++++##-#%##-==--:::....:::=*+*+++++===-:............................................-@%%#+****#%@%@@@%%@%%%%")
    print("@@@@@@@@@@@@@@@@@@@##*******#**=-.    .*++++++#*-*%%=+==-----:::::::-*****++++++===...........................................-@%%#+**##%@%%@%%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%%*****+*+.  . ...-*#+++++*#*=+%+++====----::::::-=#####******+===:........................................-@%%#+*##%%@%@%%%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%%##****##+++*#%%###*++++*%#*+=++++=======---------=#%###***####+=++-:.....................................-@%@#+*##%%%%@%@%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%####****#####***+++++*+*#%#%##++++=========--------=#%%%%%####%%%*++*===-::::.............................-@%%#+*##%%@%%%%%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%#######*************+*##%%%%%%**+++++=========-------*%%%%@%%%#%%%%#+==+=-----::::........................-@%%#+*##%%@%%%%%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%%#**#%%##************##%%%%#@%***+++++++======------=-+%%@%@@%%%%%%**##+-::::-------:.....................-@%%#+*##%%@%%%%%%%@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%%#*+%%%%#%##******###%%%%%%%%%******++++++=======-=====+%@@@@@@@@%+*###+=----=--------:...................-@%%#**#%%%@%%%%%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%%#*+%@@#+++++*##*##%%%%%########******++++++**+++====++++#@@@@@%#**#%#**++=======---:---:.................-%%%#**#%%%@%%%%%%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%%#*+#@@#===--+%%#%@@@%%####*+*#######********##***#%@@@@@@@%%%%%@@%##*****++========----=-:...............:%%%#**##%%@%@%%%%%%@@@@")
    print("@@@@@@@@@@@@@@@@@@@%##*+#@@#+===+%%%@@@@@%%#+++++##%%##########*#%@@@@@%+=---=+%@@@@@%#*+++*****+++===++==---==:.=:...........:#%%#+*##%%@%%@%%%%@%%%%")
    print("@@@@@@@@@@@@@@@@@@@%#**+#@@#+=++*%#%@%%%%##++*#***%%##########%@@@@@@@%*+#%@@@%##%%%##***+==+*##**++++++++==--==.-==-:........:*%%#+*##%%@%%@%%%%@%%%%")
    print("@@@@@@@@@@@@@@@@@%%##**+#@@#====####@%%###**#**##%%%##########@@@@@@##%%%@@@@@@##########%%#*+=*##**++++++++====-++++++++==----*%%#+*##%%@%@@%%%%@%%%%")
    print("@@@@@@@@@@@@@@@%%%%##**+#@@#=+#%%%**#@%###*####*#%%%%#########@@@#*#%%%%%@@@@@%%%%#####%@#-:-*%#+*#***++++++++***####**++====-=%@%#+**#%%%@@@%%%%@%%%%")
    print("%%@@@@@@@@@@@%%%%%%##**+#@@#*#*##%***@%%#*+%%%#**%%%%%%%%%%%#%%*+*#@@%%%@@@@@#%%%%%####%@#---:=%%#*********#****###%%%%%%###*++%%%#*****#@@%@%%%%@%%%%")
    print("%%%%@@@@@@@%%%%%%%%##**+#@@#==++*%*++%%###*+####%%%%%%%%%#%%###=.:-@@%%%@@@@%%%%%#####%@@@@##%@%#####**############%%%%%%###**+#%%#+****##%@@%%@@%%%%@")
    print("%%%%%%@@@%%%%%%%%%%##**+%@%#==+++#*+=*#####%%%%%%%%%%*===--*%@#+..:%@%%@@@@@%#######*#%%%#******##%##*##***+++***#@@%%%%%###***#%%#+***#####%@@%@@%@@@")
    print("%%%%%%@@%%%%%%%%%%%##**+%@%#+++++*+=+*##%%%%%%%%%%*=------+++#**-::*@@@@@@@%#####*###*****######%@@@#*#+-::=#**#*%#%%%%%%##**++#%%#+****#####%%@%%@@@@")
    print("%%%%@@@@@@@%%%%%%%%##***%@%*++++++++**#%%%%%%%%%*------====--*##=::=@@@@@@%###***********######%@@@%#**#--+%#++*-.. ..........-%%%#+***########%@%@%%%")
    print("%@@@@@@@@@@%%%%%%%%##***%@%*++++++++*##%%%%%%#+-=--=========--###::-%@@@%%%###************#*##%@@%#****%@@%*#%:-*=............-@%%#+***##########%%%%#")
    print("@@@@@@@@@@@@@%%%%%%##***#%%*++++++++*#%%%%%#+=============++++#%#+-:+@@@%%###****************%@%%#****+#@#+#@#-.+*-...........-@%%#+***#########%%@%##")
    print("@@@@@@@@@@@@@@@%%%%%#**+%%%*++++++++*#%%%%#+=+*+========+++++*%%%@*::-#@@%###***************%@%%#****+*+*#%@%*=:-*=...........-@%%#+***#######%@@@@@%%")
    print("@@@@@@@@@@@@@@@@@%%###**%@%#++*+++++*##%#=*##+=+====++++++++++#%%%%%+::-%@##*********#*##**#@@%#+*****+*%@@#+==-=+=...........-@%%#+***#####%@@%%%%@@@")
    print("@@@@@@@@@@@@@@@@@@%%#**+%@@#++++++***#*=-=+++++==+++++++++++++#%%@@@%%=:-+@%#**#*#########%%@%#*******%%#+-=====+==...........-@%%#+***###%@@%%@@@@@@%")
    print("@@@@@@@@@@@@@@@@@@@%#***%@@#++++**++***+=+**+++++=+++++++++++*%%@@@@%%@*::-*@@%######+:::=*#%#%%%%#*+====----+*+==-...........-@%%#****#%@@@@%@@%%%%@%")
    print("@@@@@@@@@@@@@@@@@@@%#***%@@#+++++++++++++****++++=+++=+++=+*+=-+%@@@@@@@%=:--%@@@%###%%#+:.:----:--------:=*#*+==-............-@%%#***#%@@@%@%@%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@@%##**%@@#++++++++++=++*#***+++++++==--==++++++-=#@@@%@@#=-=*@%#%%%@@%%@%#+=-::-----=*%%%##*+=:.............-@%@#+*##%@@%@%%@%%%%%%%")
    print("@@@@@@@@@@@@@@@@@@%%%#**%@@#++++++++++==+*##***+++++#*-.....:=++++++=+%@%@%%*==+%@@@@@@@@@#++++++*##****#%#*+=:...............-@%@#+*##%%@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@%%%#**%@@#++++++++++===+#%##+-....*@%%=:..:.:++++**++#@@@@%#+++%@@@@@%=:==-:::--==:-=--:-=:.................-@%@#+*##%%@@@@@@@@@@@%%")
    print("@@@@@@@@@@@@@@@@@@%%%#*+%@@#+++++++++++===+%%+::......%@#-::-::.=******=+%%%@%%***#@@@%:--:-:::::--:-==-=+=:.. ...............-@@@#+*##%%@@@@@@@@@@@%%")
    print("@@@@@@@@@@@@@@@@@@%%%#**%@@#+++++++++++===+*%@%*=--:...:::-----:..-==+**++%@@@%@##@@@%=:-:::::::::::::-=+::---................-%%%#**##%%@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@%%%#**%@@#+++++++++++*+=-:.*@@%*=-:---===-::::...---++++=#@@@%@@%###*--::::::::-----:-:=+--.................-%%%#**##%%@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@%%%#**%@@#++++++++++*##+=-:.:%%*=======-:=%#*+:...==:+***=*@@%#*#%@@%+--::::::::::::---::=-.................-@%%#**##%%@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%##*+%@@#++++++++##%%##++=--:-===++++:-**++*+:......=+***+*###%@@%%%%+--:::::::::::-----:-+-...............-@%@#+*##%@@@@%%%%%@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%#**+%@@#++++**#%%%%%###*+=+++++++*=:=#+==+*+:::.:.*#+-=***#@@%%%*+#%%*=--:::::::::-------:-++-:...........-@%@#+*##%@@@@%%%%%@@@@@")
    print("@@@@@@@@@@@@@@@@@@%%#**+%@@#++*#%%%%%%#*++*%###***+*+--**===+**+-=-==-::-*+:--=#@%+:-=+#@@%*=---:::::::--------::-==+-........-@%@#+*##%@@@@%%%%%@@@@@")
    print("@@@@@@@@@@@@@@@@@%%%#***%@@#*#%%@@%#*++++++*%%%###*=-=#+====+**+-=-+-+-*#*+++#+-=::::--=*%@@@%*=::--:::---------:::...........-@%@#**#%%@@@@%%%%%@%%%%")
    print("@@@@@@@@@@@@@@@%%%%##***%@@##%%%#*++++++++++*%@%%#==*#+++===+**+===+=*+%%#*-..-*%*--:.::-=*%@@@@@%*-:-::------::::::..........-@%@#**#%%@@@@%%%%%@%%%%")
    print("@@@@@@@@@@@@%%%%%%%%#***%@@###**++++++++++++**#@%++#*+++++++***+++*++###%#-.......+#*-::::--=*#@@@@@#-::----::::::--..........-@%@#**#%%@@@@@%%%%@%%%%")
    print("@@@@@@@@@@@%%%%%%%%%#***%@@#**++++++++++++++++*#*+##+++++++**#*+***+*++#%*-...::-:-===--=-.::-=+*%@@%%=-::::::::::=-:.........-%%@#+*#%%@@@@@@@@@%%%@@")
    print("@@@@@@@@@%%%%%%%%%%%#***%@@#+***+++++++++++*++**###**++++**#*#****#*#**+++==---=+*#**+++=::...:-=+#@@%%+--:::::::-===:........-@@@#***#%@@@@@@@@@%%%@@")
    print("%@@@@@@%%%%%%%%%%%%%#***%@@#++*****++++++++++*+*####*******##%+##%*##++++++===-=*=###+::*.=:::::-=*#@@@%*-::::::--==+=--.. ...-@@%#***##%@@@@@@@@%@@@@")
    print("%%@@@%%%%%%%%%%%%%%##**+%@@#+++**##***+++++*+++*%%**####*###%#*###*%##=:-+*++===+#*++-:.*:=:.::::-=*%@@%@*::.::::-==+++==-::..-@%@#+**###%%@@@@@%%%@@%")
    print("%@@@@%%%%%%%%%%%%%%##**+%@@#+++++*##*****++++**##*#@*+#%%%%%%*##%#*%%##*=:-+*++=+=*#%*--#-+-:::::--=#%@@@@#:...::-==+****++==--%@@#+**#####%@@@@@@@%##")
    print("@@@@@@@@%%%%%%%%%%%##**+%@@#++++++*###****++*##++++**#%*#%@@%*#%%%*@@%%#*+++*+++++*++***#=*-..::.::-*#%@@@%%-..:--==+*#%%%%%##*%%@#+**######%%@@%%####")
    print("@@@@@@@@@%%%%%%%%%%##*++%@@#++++++++**##*+*##**+++++++**%@%%%#%%%%##%@%%#*********++***#++#+*-....:=*#%@@@@%%=::-===+*#%%%%%%%%%@@#+**#######%@%%#####")
    print("@@@@@@@@@@@%%%%%%%%##*+*%@@#+++++*+++**####**+*++++++++****%%%%%@@@%*#%%###*####+::=**##+#*#*#*:..-+*#%@@@@@%@+--===++#@%%#####@@@#+**#####%@@@@%%####")
    print("@@@@@@@@@@@@%%%%%%%##***%@@#+++***+++++*###****+++++++++++++*#%%%@@@@%#*######%%#*+:.=#**#*@%#**-.-+*#%@@@@@@@@#====++-. . ...-@@@#+**###%%@%%@@@@%%##")
    print("@@@@@@@@@@@@@@%%%%%##***%@@#++++****+++++**##********+++++++***#%@%@@@@%#**#%#%%%#+==--+%#%@@%#**+:=*#%@@@@@@@@@#=+=+:... ....-@%@#+**##%@@@@@@@@@@@%#")
    print("@@@@@@@@@@@@@@@@%%%##***%@@#+++********++++*##******+*++++++****#%%@@@@@@@#*#%@@@%%%%#*%#%@@@@@#***-+#%@@@@@@@@@@%=-..........-@%@#+*#%%%@@@@@@@@%%@@@")
    print("@@@@@@@@@@@@@@@@@%%%#***%@@#+++*********+++++*###*****++++*+***##%%%%@@@@@@@%##%@%#%%*#%#@@@@@@@#***=%@@@@@@@@@@@@#...........-@%@#+*#%%@%%@@@@@@@@@@%")
    print("@@@@@@@@@@@@@@@@@@%%#***%@@#++++******+**+++==+******++++**+***#%%%%%%%@@@@@@@@%#%%%##%%@@@@@@@@%#*#+#@@@@@@@@@@@@@*..........-@@@#**#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%#***%@@#++++******+****++===+**********+**##%%%%%%%%%%@@@@@@@%#*#%%@@@@@@@%%%%#**#@@@@@@@@@@@@@@-.........-@%@#**#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%%#**%@@#++++************++===+**********##%%%%%%%%%%%%%%%@@@@@@%@%@@@@@@@%%%%%##*+%@@@@@@@@@@@@@+.........-@@@#**#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%%#**%@@#++++***************+===+****######%%%%%%%%%%%%%%%%%%######@@@@@@@@@%%%%#+. .*@@@@@@@@@@@+.........-@@@#**#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%%#**%@@#++++***********++***++===+*##%%###%%%%%%%%%%%%%%%%%%%%%###*#%%@@@@@@@%%#-.....=#@@@@@@@*..........-@@@#**#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%##**%@@#+==++*++************+**=--=+*###%%%%%%%%%%%%%%%%%%%%%%###**#**#%%@@@@@%+..........:::.............-@@@#+*#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%%#*+%@%%+=-=+++******************+=--=+**###%%%%%%%%%%%%%%%%%######*##%##*=::.............................=@@@#+*#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@%##*+#@@%=.. :++**+*******************+++++++**##%%%%%%%%%%%#######*#%###*-................................*@%%***#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@%%##***#%%@+..:::-::::::::::::::::::--------:-::::::-====----------------:. ..............................:*@%@%***#%%@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@%%%%###***#%%@%*=-------:::::::::::-------------------::::::::------------:. ...........    ...  .........-+%@%@%***#%%@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@%%%%%%%%##***##%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@#*+*#%%@@@@@%@@@@@@@@@@")
    print("@@@@@@@@@@@%%%%%%%%%%%%##**+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#***##%%@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@%%%%%%%%%%%%%%###*********************+++++++++++++++++++++++++++++++++++++++++++++++++**+++++++++*****++++++++++++***#%%%%@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@%%%%%%%%%%%%%%%%%%%#####*********************************************************************************************####%%@@@@@@@@@@@@@@@@@@@\n")
    print("You jam $500 into your phone and play Evil Pekka Barrel, which instantly three-crowns your opponent and hardware bans him from the game. You win.")
    print("Secret Ending 2: Degeneracy")



def cinema():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@#.-%@:-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@+.:#@-=+@@@@@@#+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@%%@*.:*@-.:*@@@@*.-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("% .%#  :@-..=@@@@::+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+%@@@@=+#@@@@@@@@")
    print("%..+%  .%=  =@@@=.:*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-+%@@@-=*@*=%@@@@")
    print("@  :#.  *+  =@@*.:=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-=+%@@--+%%-*@@@@")
    print("@.  *:  #+  *@@:.-#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%#*+*=-=*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:=*%@-.-#@-=@@++")
    print("@+  :.    ...::-=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.  .:---:==-+*%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%-:-*@+.:+@.:%%++")
    print("@*.      .:..:-=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= .: :-==+*+**+**#*#%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.:-==----=+@@++")
    print("@-. ....::::=+=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@= .....:-=++*###%@@@@##%@@@@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@%@@%@+ ....-:.:=:=%@")
    print("@-  .. .::-----=*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#  ..  .:-==++****#%@@@@@%%@@%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+=+#%%--::+=.   .=-+")
    print("@+...:::.::::-:::::::-+*#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=      ..:-==++===++*#%@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:=****#@@*-=@%:.    .=")
    print("@#:.:::..:::::.:-:=#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=   . . .:---===--==+*#@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%@@@@@@@@@%@%%  -...")
    print("@=. ..::.::-::--=%%*====*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%       .:-+++++++**#%@@@@@%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%###*+=+*@+:  .=")
    print("@@-:.::.:::---==+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   :.    :--+=:---=++##%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+=+**+-#@@+. -#")
    print("@@---==-----=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   . .-*%%%#*+-+*%@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%#%#++#%%@++.+@")
    print("@@-:::::-=+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%    .+#**####=-*@@####@@@@@@@%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%####%#%#***+*@%%#=%@")
    print("@%:...:-=-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*    -#%%@@%*=:-=@@==*%@@@@@@@@####################%%%%%%%%%%%%##########+=*+*+*-=+%@")
    print("@#:....-=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+-   :=:===*+=-:=%@@++*%@@@@@@%###########################################+*=--..==#@")
    print("@= . .:-=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#- :.  :=*#%=-=  :-@@*+***#@@@@%*##########################################*- :--+#@@@")
    print("%+=**##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=-. .:-=++--=. ::+@@@%**#@@@@@############################################%@@@@@@@@@@")
    print("*%***##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%:- .:-*=:=*==##@@@@@@@@%@@@@@#############################################@@@@@@@@@@")
    print("*@+**##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%*..::-:-++=-:-==+#@@@@@@@@@@@*####################################################%@")
    print("#@***##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@.. .:-+=====+*#%@@@@##%@@@%######################***********#########****#@%%%@@@@@")
    print("@****%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%%%-.--:*#*=-:---+#%@#=@@@@*##########************************************#@@%%%%%@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%@+-+-*====---=*%@@@%@@@#**#********************************************#@@%%%%%@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%@%%%+.-*+==---==*%@@@@@@@@*###********************************************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@%%%%%@%*:%=--*@@%##@@@@@@@@@@@@@%**##******************************************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%%%%%%%%%%%%%%###%%%%#+-=*@++%**%%@@@@@@@@@@@@@@@@@@@#******************************************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@-. ...=*%@%#****#**#*########**#*++++@@@**==+*@%*#@@@@@@@@@@@@@@@@@@%*++*%@@@@@@@@@@@#**********************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@#   . :***@@%%@@@%@%@@@@@@@@@@%#@@###+*@@@@#:=+==*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@********++************@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@=:    +@#%@@@@@@@@@@@@@@@@@@@@@@@@@@##%@@@@*+=+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**+++*++++++**+++*@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@-.  :#@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@%**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##++*+**+++*++++*@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++++++++++++#@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+*@@@@@@%@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+++++#@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@%%@#@@+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@%%%%*#@+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@@@%%@@@@@@@%%%%%%#%@+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@#%@@@@@@@@%%%@%%@%@+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@%@@@@%%%%*%@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@%@#%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("====*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@%##%%@@@##@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%@@%@@@@@@@%%%%@@@@@@%#@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#**")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% +@@    -@+   =@*   =@.-@@@ :@@ *     *    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+===:..::-==")
    print("@@@@@@@@@@@@@**%%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ : %@ .%= @. +@@* #@@ @.-@@@ -@@ #%# =@@ -%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*--=+-..::--=+*%")
    print("@@@@@@@@@@@@@#*%@@*-:#@@@@@@@@@@@@@@@@@@@@@@@@@@: *  @ :@# #@@% .+ #@@ %.-@@@ -@@ *## =@@ =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@====+=..::-==+#%%")
    print("@@@@@@@@@@@@@%#%@@@-+@@@@@@@@@@@@@@@@@@@@@@@@@@* @@@ +  . -%+ : =@*.. =@. . =* . -@#* =@@    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+====+:.::--=+*%%%")
    print("@@@@@@@@@@@@@@%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@%%@@@@@@@%@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+===+=.::-==++%%%@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@#**%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@%@%@@@@%%@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@++++++-.:-==++*%@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@#         .@@@@%    @@@.    @@@@@%#   -@@@            :@@     +@@@@@@@@.     @@@@@@@@    -@@@@@@@@++++*+:.--==+**%@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@.   .*#*=    #@@%    @@@.     %%%%@%   -@%@    ========*@@      %@@@@@@=      @@@@@@@-     *@@@@@@@++++*=::-==++*#@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@:   +@@@@@@    @@%    @@@.      @%@%%   -@%@    @@@@@@@@@@@      :@@@@@@       @@@@@@%       @@@@@@%+++**-::-==+**%@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@%%%@@%    @@@:   .   *@%%   -@@@    @@@@@@@@@@@   :.  #@@@@-  =    @@@@@@   :@   .@@@@@#++**=::-==+**#%@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@#   .@@@@@@@@@@@@@%    @@@:   @=   *@%   -@@@           *@@@   -#   @@@#   @    @@@@@:   %@%   +@@@@@+***-.:-=++**#@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@%   .@@@@@@@@@@@@@%    @@@.   @@+   =%   -@@@    .......%@@@   :@-  .@@   %@    @@@@*   -@@@-   @@@@@#**#::--=+**#%@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@%    @@@@@@@@@@@@@%    @@@:   @@@*       -@@@    @@@@@@@@@@@   :@@   *:  =@%    @@@@            .@@@@@**#-:-==++*#@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@:   =@@@@@@    @@#    @@@.   @@@@%      -@@@    @@@@@@@@@@@   .@@#      @@%    @@@-             -@@@@**#=--+*+*##@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@.    -==:    %@@%    @@@.   @@@@@@     -@@@    :..:::..+@@   .@@@-    #@@%    @@*   :@@@@@@@    #@@@*#%=-=*#**##@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@%         =@@@@%   .@@@:   @@@@@@@    -@@@            :@@   .@@@@   -@@@%    @@    %@@@@@@@@   .@@@*#%==*###*#%@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###%=+**##@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%%%*+**%@@@@@@@@@@\n")

print("\nYou are a high school boy who is hopelessly addicted to Clash Royale. You pull out your phone in the middle of History class because you physically can't live without it.")
start()