number_x = int(input())
count = 0
for x in range(1, number_x):
    for y in range(1, number_x):
        if x**2 + y**2 == number_x:
            count += 1
print(count // 2)
