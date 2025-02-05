sub1 = int(input("Enter the marks obtained in Maths:- \n "))
sub2 = int(input("Enter the marks obtained in History:-\n"))
sub3 = int(input("Enter the marks obtained in Geography:-\n  "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% marks ")

if(sub1+sub2+sub3)/3 < 40: 
    print("You are fail due to less total pecrentage") 
else: 
    print("Congrats !!! You have passed")