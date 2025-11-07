fav_food = ["omlit", "stake", "burger"]
fav_candy = ["kit kat", "twix", "pull an pell licorish"]
empty_list = []
numbers = [1, 2, 3, 4]

fav_food.append("pizza")
fav_food.insert(1, "pizza")
fav_food.extend(fav_candy)

fav_candy.remove("pull an pell licorish")
fav_candy.pop(1)
fav_candy.clear()

fav_candy.sort()
print(fav_candy.index("stake"))
print(len(fav_food))

print(max(numbers))
print(min(numbers))


print(fav_food)