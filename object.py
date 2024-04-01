#OOP in python(object oriented program). We deal with real time object and its entities.
class Room: #blueprint o object
    l=int(input('Enter length:'))
    w=int(input('Enter width:'))
    h=int(input('Enter height:'))

    def area(self):
        print("Area of room is ", self.l*self.w)

    def volume(self):
        print('Volume of room is ',self.l*self.w*self.h)

# area_of_room=Room()
# print(area_of_room.area())

volume_of_room=Room()
print(volume_of_room.volume())


