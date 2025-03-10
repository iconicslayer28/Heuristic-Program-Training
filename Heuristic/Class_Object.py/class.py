class TATA():
    Nexon = { 
        'Color': 'Red',
            'Sunroof' : 'Yes', 
               'Headlights' : 'Yellow',
                     }
    
    Punch = { 
        'Color' : 'Orange',
        'Sunroof' : 'No',
        'Headlights' : 'Bluishgreen'
    }

    def display(self):
        print("Horn ok please!!")
        print("Keep 6 ft distance.")

obj = TATA()
print(obj.Nexon)
print(obj.Punch)
obj.display()