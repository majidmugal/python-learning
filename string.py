# A string in Python is a sequence of characters enclosed in quotes. You can define a string using either single quotes 
# (' ') or double quotes (" "), or even triple quotes (''' ''' or """ """) for multi-line strings.


# Creating Strings:

#     Single Quote: 'hello'
#     Double Quote: "hello"
#     Triple Quote: '''hello''' or """hello""" (used for multi-line strings)


# String Operations:

# Concatenation: You can combine two or more strings using the + operator.

# str1 = "Hello"
# str2 = 'World'
# result = str1 + str2
# print(result)  # Output: HelloWorld

# Repetition: You can repeat a string multiple times using the * operator.

# str1 = "Hello"
# result = str1 * 3
# print(result)  # Output: HelloHelloHello


# Indexing: Each character in a string has an index. The index starts at 0 for the first character.
# To access these values we use `[]` operator.

# my_string = "Hello"

# print(my_string[0])  # Output: H
# print(my_string[-1])  # Output: o (Negative index starts from the end)
# print(my_string[50]) #IndexError: string index out of range


# Slicing: You can extract a substring by using slicing notation [start:end-1].
# For slicing we use `:` operator in side `[]`
# if we enter wrong index it won't give any error but can lead to blank output 

# [from:to-1:in_what_order]

# my_string = "Hello"
# where_to cuts by -1

# print( my_string[ 1: ] ) # ello

# print(my_string[ 1:4 ])  # Output: ell (Extracts from index 1 to 3)
# print(my_string[ :3 ])   # Output: Hel (Extracts from index 0 to 2)

# my_string = "0123456789"

# print(my_string[ 1:10:3 ])   # Output: 147
# print(my_string[ -8:-1 ])   # Output: 2345678
# print(my_string[ -8::-1 ])   # Output: 210
# print(my_string[ -5:1:-1 ])   # Output: 5432
# print(my_string[ -5:-1:-1 ])   # Output: <blank>

# my_string = "abcdefghijklmn"

# print(my_string[ ::-1 ])   # Output: nmlkjihgfedcba
# print(my_string[ ::-3 ])   # Output: nkheb
# print(my_string[ :: ])   # Output: nkheb
# print(my_string[ :3:-2 ])   # Output: nljhf
# print(my_string[ :-2:3 ])   #output: adgj







#my_string = "abcdefghijklmn"

#print(my_string[ ::-1 ])   # Output: nmlkjihgfedcba
#print(my_string[ ::-2 ])   # Output: nkheb
#print(my_string[ :: ])   # Output: abcdefghijklmn"
#print(my_string[ :3:-2 ])   # Output:nljhf
#print(my_string[ :-2:3 ])   #output: adgj
