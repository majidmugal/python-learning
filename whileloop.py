# while False:
#     print("hello world")
#     print("hello world") 
#     print("hello world") 

# print("out of the loop")





# counter = 1

# while counter <= 10:
#     print(counter)
#     counter +=1

# print( "final counter value is (counter)")







# counter = 1

# while counter <=20 :
#     print( counter * 1)
#     counter += 2



# num = 5
# i = 1

# while i <= 10:
#     print(num * i)
#     i += 1




# counter = 5

# while counter <= 50 :
#     print(counter * 1)
#     counter += 5



# Q. take a 3 number os imput an print the largest in them

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# largest = num1

# i = 1

# while i <= 2:
#     if i ==1:
#         if num2 > largest:
#             largest = num2
#     elif i == 2:
#         if num3 > largest:
#             largest = num3
#     i += 1

# print("largest number is ", largest)





# Q. factorial 1 to 10

# num = int(input("enter a factorial value: "))
# n = 1
# factorial = 1

# while n <= num: 
#     factorial *= n
#     n += 1

# print(factorial)

     






# counter = 1

# while counter <= 5:
#     print(counter)
#     counter += 1


# print( f"Final Counter Value is {counter}" )



# sum of 5 numbers

# sum 0
# 1 2 3 4 5
# 1
# sum 0 + 1 = 1
# 2
# sum = 1 + 2 = 3
# 3
# sum = 3 + 3 = 6
# 4
# sum = 6 + 4 = 10
# 5
# sum = 10 + 5 = 15


# counter = 1
# sum = 0

# while counter <= 5:
#     sum = sum + counter
#     print(f"Number is {counter}")
#     print(f"New sum is {sum}")
#     counter += 1

# print(sum)


# counter = 1
# mul = 1

# while counter <= 5:
#     mul = mul * counter
#     print(f"Number is {counter}")
#     print(f"New multiply is {mul}")
#     counter += 1

# print(mul)


# Sum of Even Numbers: Write a program that asks the user to enter a positive integer N. Use a while loop to iterate from 1 up to N. Inside the loop, use an if statement to check if the current number is even. If it is, add it to a running total. Finally, print the sum of all even numbers up to N.

# counter = 1
# sum = 0

# while counter <= 10:

#     if counter % 2 == 0:
#         sum = sum + counter
#         print(counter, sum)
#     counter += 1

# print(sum)



# Use a while loop to keep prompting the user to enter the password until they enter it correctly. Inside the loopU
# Use if-else statements to tell the user if their attempt was "Incorrect password. Try again." or "Password accepted!".
# Limit the number of attempts to 3.
# If the user fails 3 times, print "Account locked.".

# counter = 1
# password = ""

# while counter <= 3 and password != "123":
#     password = input("Enter your password: ")
#     if password == "123":
#         print("Login Done")
#     else:
#         print("Incorrect password")
#     counter += 1

# if counter == 4:
#     print("Account Locked.")



# Ask the user to enter an integer greater than 1. 
# Use a while loop to find and print the smallest divisor of that number (excluding 1).
# Use an if-else statement to handle the case where the number itself is prime (its smallest divisor will be itself).

# counter = 2

# number = int(input("Enter A Number: "))

# while number > 1 and  number % counter != 0:

#     print(number, counter)
#     counter += 1


# if number == counter:
#     print("Failed to find the smallest divisor as it's a Prime Number.")
# else:
#     print(f"Number is divisible by {counter}")


# Positive Number Accumulator: 
# Write a program that continuously asks the user to enter numbers.
# Use a while loop to keep taking input until the user enters a negative number.
# For each positive number entered, add it to a running total.
# Finally, print the total sum of all positive numbers entered.


# number = 0
# total = 0

# while number >= 0:

#     number = int( input("Enter A number: ")) # -1
#     if number > 0:
#         total = total + number # 150

# print(f"Sum of all values are {total}")
