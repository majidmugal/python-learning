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

a = int(input("enter a number: "))
b = int(input("enter a numebr: "))
c = int(input("enter a numebr: "))

largest = a
i = 1

while i <= 2:
    if i == 1:
        if b > largest:
            largest = b

    else:
        if c > largest:
            largest = c
    i += 1

print("largest number is ", largest)