myDict = {                                         
    "Orry" : "I'm a liver",                  
    "Gamer":"The person who plays the game ",
    "hpvictus" : "the first pc brought by my family",
    "anotherdict ": {
        "Aniket" : "The one who is learning python",
        "List" : "[1,4,5,6,7]"
    }                                                                # Dictionary stores data in a nested manner also 
                                                                   
}
print(myDict['Gamer'])
print(myDict['hpvictus'])
myDict["Orry"] = [1234]                            # Dictionary are mutable 
print(myDict['Orry'])                              
print(myDict["anotherdict "]["List"]) 