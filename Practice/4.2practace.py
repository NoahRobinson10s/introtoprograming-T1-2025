'''numbers = [1, 2, 3, 3, 4, 5]
for numbers in numbers:
    print(numbers)

for i in range(0, 100):
    print(i)

games = ["1"]

for i in range(0,5):
    print(games[1])

for i in range(0,5):
    print("rank" + str(i) + ":" + games[i])

for i in range(10,100,10):
    print(i)'''

import random
numbers = []
for i in range(0,100):
        numbers.append(random.randint(-100,100))

for i in range(0, len(numbers)):
        if numbers[i] < 0:
                numbers.pop(i)

print(numbers)
        
