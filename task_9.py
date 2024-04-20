number_n = int(input())
count_1 = 0
count_2 = 0
for x in range(0, number_n+1):
    for y in range(0, number_n + 1):
        print(x, y)
        if x == y:
            count_1 += (x + y)
        else:
            count_2 += (x + y)
count = count_1 + count_2 // 2
print(count)
