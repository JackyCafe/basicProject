
class Bike:
    __speed = 0

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self,x):
        self.__speed += x


judy = Bike()
judy.speed = 5
print(judy.__dict__)

