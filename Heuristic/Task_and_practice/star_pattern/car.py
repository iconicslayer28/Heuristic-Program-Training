for row in range (7):
    for col in range(15):
        if (row == 0 and (col > 4 and col < 10))or\
             (row == 1 and (col == 4 or col == 10)) or\
             (row == 2 and (col == 3 or col == 11)) or\
             (row == 3 and (col == 2 or col == 12))or\
                (row == 4 and ( col == 1 or col == 13))or\
                (row == 5 and ( col >= 0 or col < 14))or\
                (row == 6 and (col >= 0 or col <14)):
             
             
             
            print('*', end= ' ')
        else:
            print(' ', end= ' ')
    print()


# 13,14 = col 
# row = 1,2,3