#  Encapsulation is a core principle of Object-Oriented Programming (OOP) that involves bundling data (attributes) and the methods (functions) that operate on that data into a single unit,
# which is the class. 
# It's the practice of hiding the internal state of an object from the outside world and only exposing a controlled interface to interact with it.
# Think of a TV remote control. . The remote's buttons (the public methods) are what you use to interact with it.
# You don't know or need to know about the internal wiring, circuits, or how the infrared signal is generated (the private data and methods). The internal complexity is hidden from you, and you can only change the volume or channel through the exposed interface (the buttons).
# Key Concepts of Encapsulation
#     Data Hiding: Encapsulation restricts direct access to an object's internal data. In Python, this is achieved by convention using a single underscore (_) or, more strictly, with double underscores (__) before an attribute name. These are not truly private but signal to other programmers that the attribute is intended for internal use only.
#     Access Control: All interaction with the object's data happens through its methods. This allows you to control how the data is read (getters) or modified (setters), ensuring that the data remains in a valid state.

# In this example, the BankAcount class encapsulates the _balance data. You can't directly change the balance from outside the class. Instead, you must use the deposit() and withdraw() methods, which contain logic to ensure the operations are valid.




     



# class Car:
#     def __init__(self, brand, color):
#         self._brand = brand
#         self.__color = color

#     def show_details(self):
#         print(f"car is a {self._brand} and {self.__color}")

# a = Car("honda" , "black")


# print(a._Car__color)



# __ vs _

# It's important to understand the difference between the double and single underscore conventions:
#     __var (Double Underscore): Triggers name mangling to prevent naming conflicts in subclasses. It's a way to enforce encapsulation and a form of name protection.
#     _var (Single Underscore): This is just a convention. It signals to other developers that the variable is meant for internal use and should be treated as private, but it doesn't do anything to prevent direct access. This is the more common and preferred way to indicate "privacy" in Python.





class car :

    def __init__(self , brand , color):
        self._brand = brand
        self.__color = color

    def show_info(self):
        print(f"car brand is {self._brand} and color is {self.__color}")


class ElectricCar(car):

    def __init__(self, brand, color,battery_health):
        super().__init__(brand, color)
        self.battery_health = battery_health


    def show_info(self):
        print(f"brand is {self._car__brand} , and helath is {self.__battery_health}")

a = ElectricCar("honda" ,"white", "89%")
print(a._car__color)
print(a.battery_health)




    
    





