amount_n = int(input())
count = 0
while amount_n != 0:
    if amount_n < 4:
        pass
    elif (amount_n*3) % 2 == 0:
        count += 1
    amount_n = int(input())
print(count)
