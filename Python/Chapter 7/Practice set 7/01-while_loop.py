# i = 0
# while i<10: 
#     print("YES "+  str(i))
#     i = i+1

# print("Khatam ho gya") 


sub1 = int(input("Marks 1 :-"))
sub2 = int(input("Marks 2:-"))
sub3 = int(input("Marks 3:-"))
sub4 = int(input("Marks 4:-"))
sub5 = int(input("Marks 5:-")) 

totalmarks = (sub1+sub2+sub3+sub4+sub5)/500
percentage = totalmarks


if (percentage>=80):
    print("Grade A") 
# elif(percentage<=50):
#     print("Grade B")
elif(percentage <= 40):
    print("Grade C")
else:  
    print("Fail") 


