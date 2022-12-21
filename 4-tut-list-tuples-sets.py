book = ['History', 'Geography', 'Math', 'Computer']
book2 = ['Economics', 'Business']

# print(book[0]) # can access the index of the book like this
book.append('Hindi')

book.sort() # or book.sor(reverse = True)
print(book)
# book.extend(book2)
book.insert(0, book2) # it will insert the book2 as a list to the existing book list 
# print(len(book)) # will return the length of the book (list)

# print(type(book))

createList = list(('apple')); # we cannot use the single quote because it will be inserted like : ['a', 'p', 'p', 'l', 'e']



createList = list(("apple", "orange", "banana"))
# print(createList[1:])

# if "apple" in createList:
#     print("YES, apple is available")

createList[1] = "grapes"
createList.remove("apple")
# del createList
# createList.clear()
# print(createList.pop())

# for x in createList:
#     print(x)

# [print(x) for x in createList]



