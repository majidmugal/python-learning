# # class socilamedia():


# #     CEO = "mark"            #varible is attribue in class.  

# #     def like(self):
# #        print("liked")
# #     def comment(self):        # this is mthoad is in class and his work in body of class
# #         print("cmnnt")

# # facebook = socilamedia()

# # # print(facebook.CEO.upper)

# # # facebook.comment()

# # twitter = socilamedia()

# # twitter.CEO = "elon"

# # print(facebook.CEO)
# # print(twitter.CEO)







# class car():

#     color = "black"
#     brand = "rolls royce"
#     milage = "3mph"

#     def engine(a):
#         print("rr engine")

#     def drive(b):
#         print("driving")

#     def horn(c):
#         print("pe_pe_pe_pe")

# a = car()
# b = car()

# b.brand = "BMW"
# b.color = "blue"

# # print(a.brand)
# # print(b.brand)


# print(b.color)
# print(a.color)



# class dog:

#     def __init__(self ,abc):
#         self.abc = abc
#         print("bahiya object bn gya hai")

#     def bark(self):
#         print(self.abc)
#         print("says woof")

#     def eat(self):
#         print("hungry right now")
#         self.abc = 23


# a = dog(433)
# a.bark()
# a.eat()
    




class Dog:

    sprecies = "german_sepherd"

    def __init__(self , name = "tom" , age = 2):
        self.dogname = name
        self.age = age
        self.is_hungry = True

    def bark(self):
        print(f"{self.dogname} is woof")

    def eat(self):
        if self.is_hungry:
            print(f"{self.dogname} is eating..")
            self.is_hungry = False
        else:
            print(f"{self.dogname} is not hungry right now") 
            self.is_hungry = True


my_dog = Dog()
my_dog.bark()
my_dog.eat()
my_dog.eat()
my_dog.eat()
my_dog.eat()

    