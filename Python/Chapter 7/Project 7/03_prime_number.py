num = int(input("Enter the number:-\n"))
prime = True
for i in range(2, num):
    if (num%i == 0):
        prime = False
        break 

if prime: 
    print("This number is Prime")
else:
    print("This is not a Prime")