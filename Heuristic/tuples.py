t1 = (90,3,6,8,7,0)
t2 = ("aniket","maurya")
print("The value of t1[0]:",t1[0])
print("The value of t2[0]:",t2[0])
print("The value of t1[4]:",t1[4])

# t1[5] = 25 # Can't update the tuples
print(t1)
print(type(t2))


# Slicing 

print(t1[0:4])
print(t1[4])
print(t1[-4:])
print(t1[:-3])


#  Concatenation 

print(t1+t2) 


# Nesting 

t3 = (t1,t2) # Nesting helps creating tuple in another tuple. 
print(t3)