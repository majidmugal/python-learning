class car :
    def __init__(self , brand , milage , speed):
        self.brand = brand
        self.milage = milage
        self.speed = speed

    def __add__(self, r_value):

        return self.speed + r_value.speed

        # return self.speed + obj2.speed
    
    def __sub__(self, other):
        return self.speed - other.speed
    
    def get_info(self):

        print(f" this is {self.brand} and milag is {self.milage}")

a = car("honda", 10, 400)
b = car("bmw", 20, 200)

print(a - b)


    


    

        