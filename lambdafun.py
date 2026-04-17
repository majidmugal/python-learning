# lambda a , b : a + b

# add = lambda a , b : a + b

# print(add).   direct object call

# print(add(2,3))




####### evalute function

# command = 'print("hello world")'

# # print(command)

# eval(command)

# print = 'print("hello institute)'



#### callable function


# def simple():
#     pass

# def simple1(x):
#     pass


# print(callable(simple))



# print(callable(lambda x: x))

# file = open("majid.py")

# print(callable(open))



# def simple():
#     return("i am a simple func")

# def caller(x):
#     print(x())

# caller(simple)



########higherorder function

# def main_fun():
    

#     def add(a,b):
#         return a + b
    
#     return add

# data = main_fun()

# print(data(2,3))




def div(a,b):
    return a / b

def mul(a,b):
    return a * b

def add(a,b):
    return a + b

def sub(a,b):
    return a - b


def calculator(a, b, c):

    return a(b ,c)

print(calculator( add, 2 , 4))




