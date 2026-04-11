# class vehicle :
#     brand = "maruti"

# # class car(vehicle):
# #     pass

# # print(vehicle.brand)    




# class vehicle:
#     def __init__(self , brand ,color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"brand {self.brand} color {self.color}")

# class car(vehicle):
    
#     def wheels(self):
#         print("car have 4 wheels")

# class bus(vehicle):
#     def wheel(self):
    
#         print("bus have 10 wheels")


# # my_car= car("honda" , "white")

# # print(my_car.color)

# my_bus = bus("volvo" , "red")
# # my_bus.display_info()
# # print(my_bus.color)
# # my_bus.display_info()

# my_bus.wheel()






# class vehicle:
#     def __init__(self , brand ,color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"brand {self.brand} color {self.color}")

# class car(vehicle):

#     def __init__(self, wheels):
#         super().__init__("honda" , "white")
#         self.wheels = wheels


# a = car(vehicle )

# print(a.color)
# print(a.brand)
# a.display_info()





## multiple inheritece


# class parent_A :

#     def method_A(self):
#         print("method from parent A")

#     def test(self):
#         print("test A")

# class parentB :

#     def method_B(self):
#         print("method from parent B")

#     def test(self):
#         print("test B")

# class child(parent_A ,parentB):

#     def method_c(self):
#         print("method from Child")

#     def test(self):
#         # super().test()

#         parent_A.test(self)
#         print("test_c")
        


# child_obj = child()
# # print(child_obj)

# child_obj.method_A()
# child_obj.method_B()
# child_obj.method_c()
# child_obj.test()







# class vehicle :
#     def __init__(self , brand , color):
#         self.brand = brand
#         self.color = color

# class RTO :
#     def __init__(self, number , ownerid):
#         self.number = number
#         self.ownerid = ownerid

# class car (vehicle , RTO):

#     def __init__(self):
#         vehicle.__init__(self, "honda","color")
#         RTO.__init__(self, 2324234, "mazid")

# my_car = car()   

# print(dir(my_car))

# print(my_car.ownerid)








#######multileve + multiple inheritrnce


class parentA :
    def method_A(self):
        print(" call method A")

class parentB(parentA):
    def method_B(self):
        print("call methoad B")

class parentC:
    def method_c(self):
        print("call method c")

class child(parentB , parentC):

    def methoad_d(self):
        print("call mathod D")

obj = child()

# print(dir(obj))

obj.method_B()



