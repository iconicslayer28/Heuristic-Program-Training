Dict = { 
    "Tuples" : "They are unchangeable, contains duplicate elements and unordered",
    "Lists" : "They are changeable, contain duplicate elements and r ordered",
    "Brand" : "Bugatti",
    "Model": "Chiron",
    "Year" : "2016",
    
        "anotherdict" : {
           "Our Dict" : "Dictionary contains every kind of data",
           "sets" : "They r same in some kind", 
           "lists" : " [9,1,3,4,421,543]"
        }
    
}

print(Dict)
Dict2 = input("Enter words for ur dictionary:")       # Concatenation is not possible in dictionary.
print(Dict,Dict2)   # Nesting is possible in dictionary. 


print(Dict.keys())     # Prints the keys of dictionary
print(list(Dict.values()))  # Prints the value of dictionary 
print(Dict.items()) # Prints the keys, value for all contents of dictionary 

print(Dict.get("Tuples"))


# Dictionary can print specific keys from own dictionary.
print(Dict["anotherdict"])   
print(Dict["Brand"])


Dict["Brand"] = ["Bugatttttiiii"]
print(Dict)


updateDict = { 
    "Brand" : "Samsung",
    "Model" : "Samsung S 25+",
    "Year" : "2025",
    "AAP" : "Lost the Delhi Elections",
    "BJP" : "Won the Delhi elections",
    "Congress" : "Khata bhi nhi khol paayi congress"
}

Dict.update(updateDict) # Updating the data previous data and adding its different data.
print(Dict)


# The difference between .get() and [] syntax of dictionaries ? 


print(Dict.get("Gamer2"))   # throws the None if Gamer2 is not present 
print(Dict["Gamer2"] )      # Throws the error if Gamer2 is not present 