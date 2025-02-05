myDict = {                                         
    "Orry" : "I'm a liver",                  
    "Gamer":"The person who plays the game ",
    "hpvictus" : "the first pc brought by my family", 
    123 : 34 
    } 

# Dictionary methods  

# print(myDict.keys()) # Prints the keys of dictionary
# print(list(myDict.values()))  # Prints the value of dictionary 
# print(myDict.items()) # Prints the keys, value for all contents of dictionary 

print(myDict)
updateDict = { 
    "Hello " : " mY Love ",
    12 : 90, 
    "Orry" : " is a gay "
}
myDict.update(updateDict)  #Updates the dictionary by adding key value pairs the updateDict
print(myDict) 

# The difference between .get() and [] syntax of dictionaries ? 

print(myDict.get("Gamer2")) # throws the None if Gamer2 is not present 
print(myDict["Gamer2"] ) # Throws the error if Gamer2 is not present 
