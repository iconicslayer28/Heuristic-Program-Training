class add:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def result(self):
        print(f"The addition of {self.a} and {self.b} is {self.a + self.b}" ) 

class sub:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def result(self):
        print(f"The Subtraction of {self.a} and {self.b} is {self.a - self.b}" ) 

class mul:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def result(self):
        print(f"The Multiplication of {self.a} and {self.b} is {self.a * self.b}" ) 

class div:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def result(self):
        print(f"The Division of {self.a} and {self.b} is {self.a / self.b}" ) 

obj_1 = add
obj_2 = sub
obj_3 = mul
obj_4 = div

while True:
    print("\n1. Addition\n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
    choice = int(input("Enter ur pick: "))
    if choice == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        obj_1 = add(num1,num2)
        obj_1.result()
    elif choice ==2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        obj_2 = sub(num1,num2)
        obj_2.result()
    elif choice ==3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        obj_2 = mul(num1,num2)
        obj_2.result()
    elif choice ==4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        obj_2 = div(num1,num2)
        obj_2.result()
    else:
        print("Invalid Choice.")