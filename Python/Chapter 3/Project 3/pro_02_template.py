Letter = ''' Dear<|Name|>, Its an honour to tell you that you have been hired by ABC company. 
Yor are selected! 
Greetings. 
Have great day ahead!!! 
Date: <|Date>|
 '''
name = input("Enter Your Name\n")
date = input("Date\n")
Letter = Letter.replace("<|Name>|", name)
Letter = Letter.replace("<|Date>|", date) 
print(Letter)