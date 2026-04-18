
def square(x):

    return x * x

numbers = [2,3,4,5]

# for x in numbers:
#     print(square(x))

# squared_numbers = map(square , numbers)

# result = list(squared_numbers)

# print(result)


####one more example

# print(list(map(lambda x : x*x ,numbers)))




#########. filter method


def even(x):
    return x % 2 == 0

numbers = [1,2, 3 ,4, 5, 6]

# even_numbers = filter(even , numbers)

# result = list(even_numbers)

# print(result)


## example with lambda


even_numbers = filter(lambda x : x % 2 == 0 , numbers)

result = list(even_numbers)

print(result)





