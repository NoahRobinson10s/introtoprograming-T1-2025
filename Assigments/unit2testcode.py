#question 1
word_1 = input("what word do you what to input\n>")
word_2 = input("what word do you what to input\n>")
word_3 = input("what word do you what to input\n>")
print(f"your words were {word_1},{word_2},{word_3}")

#question 2
def add_three(x,y,z):
    print(int(x) + int(y) + int(z))
x_1 = input("what number do you what to add\n>")
y_1 = input("what number do you what to add\n>")
z_1 = input("what number do you what to add\n>")
add_three(x_1, y_1, z_1)

#question 3
def data_three():
    print(word_qusetion_3,int(intager_question_3) + float(float_qusetion_3))
    word_qusetion_3 = input("what word do you whant to put")
    intager_question_3 = input("what intager do you want")
    float_qusetion_3 = input("what float do you whant")

word_qusetion_3 = input("what word do you whant to put\n>")
intager_question_3 = input("what intager do you want\n")
float_qusetion_3 = input("what float do you whant\n")

data_three = print(word_qusetion_3,int(intager_question_3) + float(float_qusetion_3))

def skksjk():
    global wepon_2
    import random
    print("you arive on the crime scean and find a nother murder wepon")
    s = random.randint(1,2)
    if s == 1:
        wepon_2 = "knife"
        print("you find a knife as the murder weapon")
    elif s == 2:
        wepon_2 = "pan"
        print("a pan as the murder wepon")

    two_day_wrap_up(wepon_2,wepon_1,gone_1)

def two_day_wrap_up(wepon_1,wepon_2,gone_1):
    print("two murder weopons and two murders.you search the crime scean over and over agian and you find a window ajar and muddy foot steps leading to the fence you stop.you mesaure the food steps")
    print("a ladys size shoe")
    print("you go back to the police station ad look at your evedance")
    print(f"your currrent evedance is {wepon_1} was the mured wepon for the first murder and {wepon_2} was the murder wepon for the murder of {gone_1} and a ladys shoes foot print.")
    print("would you like to question someone")
    print("1.yes")
    print("2.no")
 
skksjk()