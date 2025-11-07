fav_fruits = ["strawberry", "rasberrys", "grape", "bannana", "pear"]

print(fav_fruits.index("strawberry"))
print(fav_fruits.index("pear"))

x = input("new fruit\n>")
fav_fruits.extend(x)
print(fav_fruits)