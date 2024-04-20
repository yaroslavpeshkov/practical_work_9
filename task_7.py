for x in range(1000, 9999+1):
    for y in range(1000, 9999+1):
        if 9999 < x + y < 100000:
            list_x = list(str(x))
            list_y = list(str(y))
            list_x_y = list(str(x+y))
            numbers = [list_x[0], list_x[1], list_x[2], list_x[3], list_y[0], list_y[1], list_y[2], list_x_y[4]]
            if (len(set(numbers)) == 8 and list_x[1] == list_y[3] == list_x_y[3] and list_y[0] == list_x_y[0] and
                    list_y[1] == list_x_y[1] and list_x[2] == list_x_y[2]):
                print(x, y, x+y)
