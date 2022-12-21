import time

# unordered and unchangeable
mySet = {"apple", "orange", "cherry", "apple"} # set 
mySet2 = {"Hindi", "English"}
# mySet.add("pineapple")
mySet.update(mySet2)
mySet.discard("Hello") # will not throw error if element is not present
print(mySet)
