text = input("Enter the text :\n")

if("make alot of money" in text):
    spam = True
elif("buy now" in text ):
    spam= True
elif("Click here" in text ):
    spam = True 
elif("subscribe this " in text ):
    spam = True
else: 
    spam = False 

if(spam):
    print("This text is spam ")
else:
    print("This is not a spam" )

    