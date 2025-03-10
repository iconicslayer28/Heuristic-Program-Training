class Porsche:
    def __init__(self,engine_type,car_type):
        self.car_type = car_type
        self.engine_type = engine_type
        

    def display(self):
        print(f"Car Type:{self.car_type} and Engine Type: {self.engine_type}")
    

obj = Porsche
print("\n1. 918 Cayenne \n2. 911 Carrera \n3. Macan \n4. Panamera")
car_type = int(input("Enter the Car number you wanna test: "))
print("\n1. EV \n2. Petrol \n3. Diesel")
engine_type = int(input("Enter the Engine type you want to test: "))
while True:
    if car_type == 1 and engine_type ==1:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('918 Cayenne','EV')
        obj.display()
        break 
    
    elif car_type ==1 and engine_type ==2:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('918 Cayenne','Petrol')
        obj.display()
        break 
    
    elif car_type ==1 and engine_type ==3:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('918 Cayenne','Diesel')
        obj.display()
        break 
    
    elif car_type ==2 and engine_type ==1:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('918 Carrera','EV')
        obj.display()
        break
    
    elif car_type ==2 and engine_type ==2:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('918 Carrera','Petrol')
        obj.display()
        break
    
    elif car_type ==2 and engine_type ==3:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('918 Carrera','Diesel')
        obj.display()
        break
    
    elif car_type ==3 and engine_type ==1:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('Macan','EV')
        obj.display()
        break
    
    elif car_type ==3 and engine_type ==2:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('Macan','Petrol')
        obj.display()
        break 
    
    elif car_type ==3 and engine_type ==3:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('Macan','Diesel')
        obj.display()
        break 
    
    elif car_type ==4 and engine_type ==3:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('Panamera','EV')
        obj.display()
        break 
    
    elif car_type ==4 and engine_type ==3:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('Panamera','Petrol')
        obj.display()
        break 
    
    elif car_type ==4 and engine_type ==3:
        experience = str(input("How was ur experience?"))
        rating = float(input("What rating you wanna give to this car(Out off 5)?\n"))
        obj = Porsche('Panamera','Diesel')
        obj.display()
        break 
    else: 
        print("Invalid Choice.")