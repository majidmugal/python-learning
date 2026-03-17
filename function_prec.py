#type of functio

#inbuilt function 
#custom function

# a = [1,2,3,5,6,7,8,9]

# print(sum(a))

# print(max(a))
# print(min(a))


# a = [1,2,3]
# b = [2,3,4]

# print(tuple(zip(a,b)))


# for a , b , c zip in (1 ,2 ,3):

    # print("a,b,c")


# Every function has two main parts: the definition and the call.

# Defining a Function
# You define a function using the def keyword, 
# followed by the function name, parentheses (), and a colon :
# The code inside the function must be indented.

# Syntax:
# def function_name():
#     print("Hello from inside the function!")

# function_name()




# Parameters and Arguments (Inputs)

# Functions often need to work with different pieces of data. 
# You can pass information into a function using parameters and arguments.
#     Parameters: The names you define in the function's parentheses when you create it. 
#     Arguments: The actual values you pass into the function when you call it.

# Example:



# def greet(name):

#     print(name.upper())

# greet("mazid")


 #Doc Strings
# def cap_str( name ):

#     """
#     This Function takes a string and it print it's Upper Case
#     """

#     print(name.upper())

# cap_str("majid")




# Functions with Multiple Parameters
# You can define a function with multiple parameters, 
# separated by commas. 
# The arguments you pass when calling it will be assigned to the parameters
# in the same order.


# def calculate_sum(num1 , num2):

#     total = num1 + num2
#     print(total)

# # calculate_sum(7,4)
# calculate_sum("hello" ,"world")



# def test(a,b,c):
#     print(a,b,c)

# test(2,3,4)


# Positional and Keyword Arguments
# You can call a function in different ways based on how you pass arguments.
# Positional Arguments
# The arguments are matched to parameters based on their position or order. This is the method we've used so far.
# Example:


# def display_info(name,age):

#     print(name,age)

# display_info("majid" , 27)



# def information(name, age, city , num):
#     print(name,age, city, num)

# information("majid",27,"bidasr", 7737713356)


# def display_info(name, age , city ="bidasr", num = 77377122):

#     print(name,age,city,num)

# display_info("majid",25,)



# def display_info(name, age, city, school, number):

#     print(name , age ,city , school ,number)

# display_info(number="13141" , school ="ads", city="bidasr", age=23,name="majid")
# display_info("majid",27, city="bidasr" , school="ABC" , number=712727,)
# display_info( collage="Test", number=23232235, city="sdfsdaf", "Vipin", 45 )
# display_info( name="vipin", 34, "Jaipur", "tets", 42424 )



#default argument

# def greet_with_default(name , message="Hello"):
#      print(f"{name}, {message}!")

# greet_with_default("majid", "how are you")


# def display_info(name, age, course, city="Jaipur", collage="ABC", number=66543):
#      print(f"Name: {name}, Age: {age}, {city}, {collage}, {number}, {course}")

# display_info("majid", 27,"bca", "bidasar")




def calculate_average(*numbers):

    print(numbers)

# calculate_average()

# calculate_average(1,2,3,4,5,6,7,7,8,"abc" , {name : majid})




# def mix_func(*numbers):

#     print(numbers)

# mix_func(1,2,3,4,5,6,7,7)



# def show_profile(**user_info):

#     print(user_info)

# show_profile(name = "mazid" , city = "bidasr" ,age = 23)



#scope of varible



























    




