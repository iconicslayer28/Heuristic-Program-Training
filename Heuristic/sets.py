s = {1,45,23345,8765,321,456}
s1 = {100,12,1,45}
print(type(s))
print(s)

#  We can also print the empty sets
s2 = {}
print(s2) 


s.add(29)
s.remove(23345) 
# s1.add({"AnotherDict" : "Dictionary"})  # Dictionary and list can't be added in the set or empty set. 
# s1.add([1,2,3])
s1.add((12345,12345,98765) )        # Tuples can be added in the sets.
s1.pop()
print(s)
print(s1)
