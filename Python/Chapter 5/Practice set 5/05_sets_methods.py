# set methods 

m = set()
print(type(m))
print(m)

#Adding value in the empty sets 

m.add(2) 
m.add(1)
m.add(1) #Adding a value repeatedly cannot change sets 
# m.add([1,2,3,4,5])  # List can't be added into the set  
m.add((1,2,3,4,5)) #Tuple can be added into the set or empty set
# m.add({1:0}) #Dictionary can't be added into the sets 
print(m) 

# lENGTH of an item 
print(len(m)) # Prints the length of the sets 

#Removal of an item 
m.remove(2) 
# m.remove(15) # Throws an error while trying to remove 15 from the set which is not present 
print(m) 

print(m.pop())
print(m)  




