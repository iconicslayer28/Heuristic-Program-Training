sub = int(input("Enter the marks:-\n"))

if sub>=90:
    Grade = "Excellent"
elif sub>=80:
    Grade = "A"
elif sub>=70:
    Grade = "B"
elif sub>=60:
    Grade = "C"
elif sub>=50:
    Grade = "D"
elif sub>=40:
    Grade = "E"
else:
    Grade = "Fail"

print("Your Grade is ",Grade) 