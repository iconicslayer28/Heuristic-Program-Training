#problem statement = add(get a predefined variable carrying a number) and print a number(input of the number must be handed over to the user) until the user commands to stop in words.

a =10

while(1):
    b = input("Enter the number: ")
    if b == "stop":
        break
    elif b!= "stop":
        c = int(b)      # typecastiing is done for in case of user gives the value in int() in place of str(). 
        a = c+a         # Another way of adding can accept [ a+= c ] where the new value of c that was stored in b is added with the value of a. 
        print(a)

# Another way of doing the same thing.
while(1):
    num1 = input("Enter the number: ")
    if num1 == "stop":
        break
    elif num1 != "stop":
        b = int(num1)
        a += b
        print(a)