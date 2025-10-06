def greet():
    print("hello world")

def add(x,y):
    print(x+y)

add(10,30) 

def calculate_tax(item,price,rate):
    print("tax price for {item} + (price),{rate}")
item = input("enter price for item\n>")

price = input("enter price for price\n>")

rate = input("enter price for rate\n>")

calculate_tax("starbucks" , 7.99, 0.6825)

#create a functon called add_five_numbers that takes five parameters.
#-one for esch number
#print the sum of the five numbers
#run the function three times with diffrent arguments.

def add_five_numbers():
    print("add five numbers")

add_five_numbers(10,20,30,40,50)

def full_name(a,b,c,d):
    print(a + "" + b)
a_a = input("first name\n>")
b_d = input("input last name\n>")

full_name(a_a + b_d)

def area_calculator(area,area_2):
    print(area + area_2)

area_calculator(10,2)

def word_smash(word,smash):
    print(str(word) + str(smash))
word_smash("cat","dog")

#print string a number of times
#two perameters 
def echo(word,times):
    print(str(word)*times)
echo("well", 1)

#one paramiter
#print happy birhtday song for there name
def happy_birthday(name):
    print("happy birthday to you , happy bitrthday to you,happy birthday to you" + str(name) + "happy birthday to you")
    