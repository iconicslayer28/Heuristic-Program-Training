for row in range (7):
            for col in range(20):
                if (row == 0 and (col >= 0 and col < 15 ))or\
                     (row == 1 and (col == 0 or col == 15 ))or\
                        (row == 2 and ( col == 0 or col == 16))or\
                        (row == 3 and ( col == 0 or col == 17))or\
                        (row == 4 and ( col == 0 or col == 18))or\
                        (row == 1 and ( col == 9 ))or\
                        (row == 2 and ( col == 9 ))or\
                        (row == 3 and ( col == 9 ))or\
                        (row == 4 and ( col == 9 ))or\
                        (row == 5 and ( col >= 0 or col < 16))or\
                        (row == 6 and ( col >= 0 or col < 16)):
                    
                    print('*', end= ' ')

                else:
                    print(' ', end= ' ')
            print()


# rows 7 and 8 are used for wheels.
#  Rest all are used for forming the vehicles. 
# Counting of the rows and columns starts from zero(0). 