for row in range(3):
    for col in range(15):
        if (row == 0 and ( col == 0 or col == 14))or\
            (row == 0 and (col == 2 or col == 12))or\
            (row == 0 and (col == 5 or col == 10))or\
            (row == 0 and (col == 7 or col == 8))or\
            (row == 1 and (col == 1 or col == 13))or\
            (row == 1 and (col == 6 or col ==9)):
            
            print('*', end= ' ')

        else:
            print(' ', end= ' ')
    print()
