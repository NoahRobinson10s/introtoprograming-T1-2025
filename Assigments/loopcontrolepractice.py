number_line = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,26,17,18,19,20]
for i in number_line:
    if i == 15:
        print("found 15")
        break
    print(i)

for i in range(1,31):
    if i % 2 == 0:
        continue
print(i)

for i in range(1,10):
    if i == 1:
        print("new feature will be added later")
        pass
        break
    else:
        print(i)

for i in range(10,0,-1):
    if i == 5:
        continue
print(i)

list = [1,-2,-3,-4,5,6,7,8]
for i in list:
    if i < 0:
        break
    sum += i
print(sum)




