import random # Random is imported. 

heading = '''Welcome to AARAMBH 3.0'''
print(heading.center(50, ))
print("-------------------------------------------------")

print('''This is more than a fest—it's a feeling, an emotion, and a memory in the making!'''.center(50, ))
print("Good vibes, great company, and a whole lot of fun—welcome to the ultimate celebration!".center(20, ))
print("-------------------------------------------------")


# Details will be entered by the input function. 

Name = input("Enter your name: ")
cl = input("Enter your Course Year: ")
field = input("Enter your field: ")

print("List of Events and Days ")              # They can be printed in this manner also.   
print("1. Tie Day")                            # print("\n1.'Tie Day'\n2. 'Mismatch Day'\n3. 'Traditional Day'\n4. 'Twinning day' \n 5. 'Gang Day' \n 6. 'Bollywood Day' \n7. 'Kratex' ") 
print("2. Mismatch Day")                        
print("3. Traditional Day")            
print("4. Twining Day")
print("5. Gang Day")
print("6. Bollywood Day")
print("7. Kratex ")



choice = int(input("Enter your choice:"))        # Choice of the events can be picked from the above list in integer form. 

if choice == 1:
    age = int(input("Enter your age: "))
    
    if age<= 0:            # Age less than or equal to zero won't be accepted here. 
        print("Invalid age.")
    elif age<= 20:
        print("Please visit the Aarambh fest on 17 feb for tie day.")
        print("Wear a green tie!!!")
        print("Tied up in style, but never in trouble!")
    elif age >=21:
         print("Please visit the Aarambh fest on 17 feb for tie day.")
         print("Wear a blue tie!!!")
         print("A tie is just a fancy leash to keep us from running away from responsibilities!")

if choice == 2:
        age = int(input("Enter your age: "))                # Age is just an option here no specific use. 
        print("Please visit the Aarambh fest on 18 feb for mismatch day.")
        
        randNo = random.randint(1,3)                # randNo is the vaiable assigned for picking the random number between 1 and 3. Th enumbers are picked by the random function itself that was impoted in the 1st line.  
        if randNo == 1:
            print("If fashion is an art, consider me abstract!")            # For printing the different cheesy lines the randint i.e. an built-in function of python is used. 
        elif randNo ==2: 
            print("We may not match, but we’re a perfect pair!")
        elif randNo ==3:
            print("My fashion sense took a day off… but my confidence didn’t!")
            
if choice == 3:
    print("Please visit the Aarambh fest on 19 feb for Traditional day.")
    print("And don't dare to miss this day becz we gonna celebrate the B'day of Chhatrapathi Shivaji Maharaj!!")
    
    randNo = random.randint(1,3)
    if randNo == 1:
        print("Please visit the Aarambh fest on 18 feb for mismatch day.")
    elif randNo == 2:
        print("Wearing my roots, and they look fabulous!")
    elif randNo == 3:
        print("Not just wearing tradition, but carrying a legacy!")

if choice == 4:
    print("Please visit the Aarambh fest on 20 feb for Twinning day.")
    randNo = random.randint(1,3)
    if randNo == 1:
        print("Twinsies today, partners in crime forever!")
    elif randNo == 2:
        print("If twinning was a sport, we’d take the gold!")
    elif randNo == 3:
        print("Twinning and winning—because one of us wasn’t enough!")

if choice == 5:
    print("Please visit the Aarambh fest on 21 feb for Gang day.")
    randNo = random.randint(1,3)
    if randNo == 1:
        print("Gang’s so legendary, even history takes notes.")
    elif randNo ==2:
        print("If loyalty was currency, we’d be billionaires.")
    elif randNo == 3: 
        print("Family by choice, trouble by default.")

if choice == 6:
    print("Please visit the Aarambh fest on 22 feb for Bollywood day.")
    randNo = random.randint(1,3)
    if randNo ==1:
        print("Aaj mood filmy hai, toh zindagi bhi ek blockbuster lagegi!")
    elif randNo ==2:
        print("Itna filmy pose marenge, ki Karan Johar bhi casting ke liye call kare!")
    elif randNo ==3: 
        print("Mere pass maa nahi hai… par ek solid Bollywood outfit hai! ")
        
    
if choice == 7: 
    print("Be present for the freshing and the energetic concert of Kratex on 23 Feb form 6pm onwards in Indala Institiue of Engineering.")
    randNo = random.randint(1,3)
    if randNo == 1:
        print("No stress, just bass—KRATEX is in the house, let’s RAGE!")
    elif randNo == 2:
        print("Lights flashing, beats dropping—when KRATEX takes over, the night never stops!")
    elif randNo == 3:
        print("Turn up the volume, lose yourself in the vibe—KRATEX is about to take you on a sonic ride!")
else: 
    if choice != choice:            # If the choice is unmatched it will throw this particular line. 
        print("You made an invalid choice.")
print("--------------------------------------------")
print(f"Thank you for participating in Aarambh 3.0 *{Name}*.\n You have participated in *{choice}* event.")            # The choice line is optional. 
