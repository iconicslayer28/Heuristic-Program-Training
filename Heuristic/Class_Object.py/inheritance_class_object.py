class add:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def result(self):
        print(f"The addition of {self.a} and {self.b} is {self.a + self.b}" ) 

class child(add):
        pass

obj_1 = add(10,20)
obj_1.result()