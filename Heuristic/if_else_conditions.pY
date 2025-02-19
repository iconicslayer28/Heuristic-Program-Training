print("Welcome to the Indala college fest!!! \n It's an pleasure to have you in our college fest.")
a = str(input("Enter Your name:"))
print("Pick your interest")
print("1.Bollywood Room")
print("2.Ghost Room")
print("3.Indala Techno park")
print("4.Cultural Room")
print("5.Music & Dance group")
print("6.Sports and Games")

select = int(input()) 


if (select==1):
        print("Let's get mesemerized into the beautiful bollywood culture!!! \n Kindly visit the room 301")
elif (select==2):
    print("If u r afraid of Kindly go to room 101")
elif (select==3):
    print("kindly go to room 201")
elif(select==4):
    print("Kindly go to room 205")
elif(select==5):
    print('Kindly go to room 200')
elif(select==6):
    age = int(input("Enter Your age:"))
    if age < 0:
        print("Invalid age")
    else:
        if age<=25:
            print("Go to the pharmacy department")
        else:
            print("Go to the Engineering department")       
else:
    print("It looks like you aare not intersted in any of the event.")
    print("So,")
    print("You can attend auditorium")

print("Thanks for visiting out college")


#  Checking the positive,negative or zero


num = int(input("Enter your number here:"))
if num == 0:
    print("The value is Zero.")
else:
    if num<=0:
        print(f"The number {num} is Negative.")
    elif num>=0:
            print(f"The number {num} is Positive.")
            




