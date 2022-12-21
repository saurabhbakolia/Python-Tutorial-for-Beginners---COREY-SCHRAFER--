# tuple is immutable

tuple1 = ("apple", "orange", "grapes")
tuple2 = ("1", "2", "3", "4", "5", "6")
# tuple1[0] = "mango" # tuple doesn't support items assignment

# (apple, *remain) = tuple1
tuple3 = tuple1 + tuple2
print(tuple3.index("1"))