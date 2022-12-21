def greet(**name):
    print("Hello!" + " " + name["who"])


greet(who="Emilia", second="John")

# * means expecting tuple and ** means expecting dictionary
