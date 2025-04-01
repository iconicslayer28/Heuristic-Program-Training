for row in range(3):
    for col in range(15):
        if (row == 0 and (col == 1 or col == 3))or\
           (row == 0 and (col == 11 or col == 13))or\
            (row == 1 and (col == 2 or col == 12)):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()