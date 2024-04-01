class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price


    def show(self):
        print('Details: ',self.name,self.color,self.price)

    def max_speed(self):
        print("Vehicle max speed is 150.")

    def change_gear(self):
        print('Vehicle change 6 gear.')

class Car(Vehicle):
        def max_speed(self):
            print("Car max spped is 240.")
        
        def change_gear(self):
            print("Car change 6 gear.")

car= Car('Car 1','Red',200000)

car.show()
car.max_speed()
car.change_gear()
