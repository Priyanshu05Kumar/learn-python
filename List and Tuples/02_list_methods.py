# List are mutable means it can be change original list
# String is immutable
#Tuple is immutable data type in python i.e Cannot be changed
friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]
print(friends)

friends.append("Harry") # append = insert at the end
print(friends)

l1 = [1,34,62,2,6,11]
#l1.reverse()
# l1.sort()
#l1.insert(2,33333) # insert 33333 at index 3
print(l1.pop(3)) #delete element at 3rd index and return value
l1.remove(11)
print(l1)
