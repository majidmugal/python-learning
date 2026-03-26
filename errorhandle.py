# Errors are an unavoidable part of programming. 
# Error handling is the process of anticipating and managing these errors
# so your program doesn't crash unexpectedly. 
# In Python, this is primarily done using exception handling.

# An exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions.

# The try...except Block
# The try...except block is the fundamental tool for handling exceptions. It works like this:
#     The code inside the try block is executed normally.
#     If an exception occurs within the try block, 
#     the rest of the try block is skipped.
#     The program then looks for an except block that matches the type of exception that occurred.
#     The code inside the matching except block is executed.






# try:
#     number = int(input("please enter a value"))
# except:
#     print("enter only digit")




# a = int(input("enter a value: "))
# b = int(input("enter a value: "))

# # print(a/b).   problem

# try:
#     print(a/b)
# except:
#     print("can not divided by any number with 0")



# try:
#     a = int(input("enter a value: "))
#     b = int(input("enter a value: "))
#     print(a/b)

# except ValueError:
#     print("enter only didgit")
# except ZeroDivisionError:
#     print("can not divided by zero")





# try:
#     a = int(input("enter a value: "))
#     b = int(input("enter a value: "))
#     print(a/b)

# except ValueError or ZeroDivisionError:
#     print("enter only didgit")
# except:
#     print("can not divided by zero")



# try:
#     my_list = [0,1]
#     user_input = int(input("enter an index: "))

#     print(my_list[user_input])

# except (IndexError,ValueError) as e:

#     print(e)




# try:
#     a = int(input("enter a number: "))
# except:
#     print("type conversion error").   
# else:
#     print("no error")    # this is only for true condtion conformation
# finally:
#     print("i will run all of cost")


# a = ""
# b = "fjj"
# c = 678
# print(locals()).    this is help to find the all variables





# now creating ERROR

# age = int(input("enter your age: "))
# if age >= 18:
#     print("you can vote")
# else:
#     raise ValueError("you cant vote")



# def test():

#     try:
#         return 1
#     finally:
#         return 2
    
# print(test())




# try:
#     # Code that might raise an exception
#     numerator = 10
#     denominator = 0
#     result = numerator / denominator  # This will cause a ZeroDivisionError
#     print(result)
# except ZeroDivisionError:
#     # This code runs if a ZeroDivisionError occurs
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     # This code would run if a ValueError occurred
#     print("Error: Invalid value was provided.")

# In this example, the try block is executed. When the ZeroDivisionError occurs, the program jumps to the corresponding except block and prints the error message.
# The print(result) line is never reached.


# Common Exception Types
# Python has many built-in exceptions to handle different types of errors. It's good practice to handle specific exceptions rather than a general one. Some of the most common exceptions are:
#     ZeroDivisionError: Raised when you divide by zero.
#     TypeError: Raised when an operation is performed on an object of an inappropriate type (e.g., adding a string and an integer).
#     ValueError: Raised when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert "hello" to an integer with int("hello")).
#     NameError: Raised when a variable is not found.
#     IndexError: Raised when a sequence index is out of range.
#     KeyError: Raised when a dictionary key is not found.
#     FileNotFoundError: Raised when a file cannot be found.

# You can handle multiple exceptions in a single except block using a tuple.


