myDict = { 
    "pankha" : "Fan" ,
    "kursi" : " Chair",
    "basta" : " Bag"  
    } 
print("Options are:- ",myDict.keys())
a = input ("Enter the Hindi word to find:-\n ") 
# print("The meaning of the word is :-", myDict[a])

# Below line will not throw error if the key is not present the dictionary 
print("The meaning of the word is :-", myDict.get(a))
