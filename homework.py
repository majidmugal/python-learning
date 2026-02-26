 

'''
# HOMEWORK

#a = 9
#b = 12
#c = 3
#x = a - b / 3 + c * 2 - 1
#y = a - b / (3 + c) * (2 - 1)
#z = a - (b / (3 + c) * 2) - 1
#print("X = ", x)
#print("Y = ", y)
#print("Z = ", z)


#a = 9
#b = 12
#c = 3

#x = a - b / 3 + c * 2 - 1

#b / 3 = 12 / 3 = 4
#c * 2 = 3 * 2 = 6

#x = 9 - 4 + 6 - 1

#9 - 4 = 5
#5 + 6 = 11
#11 - 1 = 10

#(x = 10.0)



#y = a - b / (3 + c) * (2 - 1)

#y = 9 - 2 * 1
#2 * 1 = 2
#9 - 2 = 7

#3(y = 7.0)



#z = a - (b / (3 + c) * 2) - 1

#z = 9 - 4 - 1
#9 - 4 = 5
#5 - 1 = 4

#(z = 4.0)



#x = 10.0
#y = 7.0
#z = 4.0

#print("x = ", 10.0)
#print("y = ", 7.0)
#print("z = ", 4.0)




#Q.2 = > 





#1. 10 or 20
 -> 10


#2. 0 and 50 
    -> 0

 
#3. "" and "Hello" 
    -> ""


#4. 100 or 0 and 50
    (0 and 50) (100 or 0)	
     -> 100


#5. False or 0 or "Python"
    -> "python"

    
#6. 1 and 2 or 3 and 4
   ( 1 and 2) ( 3 and 4)
    (  2 or 4 )

-> 2


#7. [] or {} and "Done"

# ({} and "Done" ) ( [] or {} )
 
-> {}


#8. "A" and "" or "C"
  
   # -> "c"	'''
# if True : 
# 	 print("hello")
#        print("world") 										


# //q.1 = grade calculator


# marks = int(input("enter your marks"))

# if marks > 90:
#     print("grade A+")
# elif marks > 70:
#     print("grade is b")
# elif marks > 50:
#     print("grade is c")
# elif marks > 40:
#     print("grade is d")
# else:
#     print("failed")


#Q.2 
# number = int(input("enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("number is divisable by both")
# elif number % 3 == 0 :
#     print("number is divisable by 3")
# elif number % 5 == 0 :
#     print("number is divisable by 5")

# else:
#     print("number is not divisable by both ")



#Q3. even or od

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("The number is Even.")
# else:
#     print("The number is Odd.")





# Q.4 Age Category Checker Program

# age = int(input("Enter your age: "))

# if age <= 10:
#     print("You are a Child.")
# elif age <= 18:
#     print("You are a Teenager.")
# elif age <= 35:
#     print("You are an Adult.")
# else:
#     print("You are a Senior.")






# username = input("enter your username: ")
# if username == "admin":
#     print("you can add other")
# else:
#     print("you can't add")



# match case 

# char = input("enter only one chracter: ")

# match char:

#     case "a":
#         print("vowel")
#     case "e":
#         print("vowel")
#     case "i":
#         print("vowel")
#     case "o":
#         print("vowel")
#     case "u":
#         print("vowel")
#     case _:
#         print("consonant")




# number = int(input("enter a number: "))

# match number :
#     case 1:
#         print("sunday")
#     case 2:
#         print("monday")
#     case 3:
#         print("tuesday")
#     case 4:
#         print("wednesday")
#     case 5:
#         print("thursady")
#     case 6:
#         print("friday")
#     case 7:
#         print("saturday")
#     case _:
#         print("invalid number")


# number1
# number2
# operator

#a = int(input("number1: "))
#b = int(input("number2: "))
#c = input("enter a operator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /, %): ")

if operator == "+" :
    print("result", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "%":
    print("Result:", num1 % num2)

else:
    print("Invalid operator")





 

