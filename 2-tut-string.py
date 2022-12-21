# # define the variables in the proper name. 
# # To use the quote inside the string use the different quote syntax for the string "hello's world!" => this is correct. and 'hello's world' => this is incorrect


# message = "Hello's World!" + " " + "I am a programmer!"

# print(message.__len__()) # give the length of the string
# print(message.lower()) # return the string in lower case
# print(message.upper()) # return the string in upper case
# print(message.capitalize()) # return the string in capitalized
# # print(dir(message)) # return the directory))

# # message = "{} {}".format("Hello", "Programmers!")
# name = "John Doe"
# status = "Programmer"
# message = f"{name} {status}"
# print(message)



# multiple_string = """           I can anything inside this multiple_string. 
# whatever             I want to add."""
# print(multiple_string)
# print(len(multiple_string))
# print("can" in multiple_string)

# # for x in multiple_string:
# #     print(x) 
# # print(message[0])
# # print(message[1:4])
# # print(message[2:])
# # print(message.replace('Doe', 'Soldi'))

# # print(multiple_string.strip()) # strip will remove all the white spaces before and after the text 


message = "hello,world"
print(message.count("d"))
print(message.split(',')) # return the array of substring separated by the separator 
