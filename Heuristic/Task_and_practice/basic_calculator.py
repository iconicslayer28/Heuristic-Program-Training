saranash = "Python based calculator"
print(saranash.center(50, ))


def div (a,b):                # Def function is used for storing the data of the calculation. Fpr all the methods. 
    return a / b

def mul (a,b):
    return a*b

def add (a,b):
    return a + b 

def sub (a,b):
    return a - b

def sq(a):
    return a**2

def cb(a):
    return a**3

def sqrt(a):
    if (a == 0 or a == 1):
        return a
    else:
        return int(a**(0.5)) 

def cbrt(a):
    return a**(1/3)

def exp (a,n):
    return a**n

def fact(a):
    if a == 0:
        return 1
    else:
        return a*fact(a-1)

def Asquare(a):
    return a*a

def Arectangle(a,b):
    return a*b

def Vcube (side):
    return side**3

def Vcuboid(p,q,r):
    return p*q*r*1

def main():
    while True:

        print("Enter your choice:")
        print("1. Division")
        print("2. Multiplication")
        print("3. Addition")
        print("4. Subtraction")
        print("5. Square")
        print("6. Cube")
        print("7. Square root")
        print("8. Cube root")
        print("9. Exponential")
        print("10. Factorial")
        print("11. Area of Square")
        print("12. Area of Rectangle")
        print("13. Volume of Cube")
        print("14. Volume of Cuboid")
        print("15. Exit")

        choice = int(input("Enter Your Choice:"))



        if choice == 15:
            break 

        elif choice == 1:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            # print(f"The division of {a} and {b} is {div(a,b)}")        # This is also an way to use the f string (formatted string) in print. 
            print(f" {a} / {b} = {div(a,b)}" )                          # f string is used for replacing the value of whatever variable is used in {}. 

        elif choice == 2:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            if b == 0:
                print("The denominator can't be negative, since the value will be infinite.")
            else:
                # print(f"The multiplication of {a} and {b} is {mul(a,b)}")
                print(f" {a} * {b} = {mul(a,b)}" )              

        elif choice == 3:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            # print(f"The addition of {a} and {b} is {add(a,b)}")
            print(f" {a} + {b} = {add(a,b)}" )

        elif choice == 4:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            # print(f"The subtraction of {a} and {b} is {sub(a,b)}")
            print(f" {a} - {b} = {sub(a,b)}" )

        elif choice == 5:
            a = float(input("Enter the first number: "))
            # print(f"The square of {a} is {sq(a)}")
            print(f" {a}^2 = {sq(a)}" )

        elif choice == 6:
            a = float(input("Enter the first number: "))
            # print(f"The cube of {a} is {cb(a)}")
            print(f" {a}^3 = {cb(a)}" )

        elif choice == 7:
            a = float(input("Enter the first number: "))                 # This can throw an incorrect answer. 
            # print(f"The square root of {a} is {cb(a)}")
            print(f" {a}^(1/2)= {sqrt(a)}" )

        elif choice == 8:                                                # This can throw an incorrect value.
            a = float(input("Enter the first number: "))
            # print(f"The cube root of {a} is {cb(a)}")
            print(f" {a}^(1/3) = {cbrt(a)}" )

        elif choice == 9:
            a = float(input("Enter the first number: "))
            n = float(input("Enter the second number: "))
            # print(f"The exponential of {a} is {exp(a,n)}")
            print(f" {a} * {b} = {exp(a,n)}" )

        elif choice == 10:
            a = float(input("Enter the first number: "))
            # print(f"The factorial of {a} is {fact(a)}")
            print(f" {a}! = {fact(a)}" )

        elif choice == 11:
            a = float(input("Enter the side of square: "))
            print(f"The Area of Square of side {a}={Asquare(a)} cm")


        elif choice == 12:
            a = float(input("Enter the length of rectangle: "))
            b = float(input("Enter the breadth of rectangle: "))
            print(f"The Area of Rectangle={Arectangle(a,b)} cm")

        elif choice == 13:
            a = float(input("Enter the side of Cube: "))
            print(f"The Volume Cube {a} cm={Vcube(a)} cm")

        # elif choice == 14:                                # It can also throw an error. 
        #     a = float(input("Enter the length of Cuboid: "))
        #     b = float(input("Enter the breadth of Cuboid: "))
        #     b = float(input("Enter the height of Cuboid: "))
        #     print(f"The Volume of Cuboid is {Vcuboid(p*q*r*1)} cm")

        else:
            print("Invalid choice.")
            print("Please try again.")


if __name__ == "__main__":
    main()








