# While using the functions of python. 

def percent(marks): 
    return (sum(marks)/400)*100

marks1 = [64,56,99,85]
percentage1 = percent(marks1)

marks2 = [99,87,65,36] 
percentage2 = percent(marks2)

print(percentage1,percentage2)


# Without using function of python. 

marks1 = (65,55,92,65)
percentage1 = (sum(marks1)/400)*100

marks2 = [45,65,98,78]
percentage2 = (sum(marks2)/400)*100 

print(percentage1,percentage2)