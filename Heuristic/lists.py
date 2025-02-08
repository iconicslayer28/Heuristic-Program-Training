list = ["aniket", 2,4,5,12,2]

#  Built-in functions for list

# Updating the list
list.append(24)         
list.insert(2,900) 


#  Removing the elements
list.remove("aniket")


# Sorting the elemnets in the list. 
list.sort()
list.reverse()
print(list)


list.count(5)
print(list)


#  Slicing in list. 


list2 = ["SANDESH","jayesh","aDARSH", "Aniket"]
list3 = ["Event", "hANDLER", 45,69,10, 'Jaipur is known as the pink city']
print(list2[0:2])
print(list2[1:4])
print(list3[-4:])
print(list3[-6:-1])


# Concatenation of different list. 
l = list + list2 + list3        # Lists contain duplicate data 
print(l)