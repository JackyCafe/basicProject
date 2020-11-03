class Bike:
    speed = 0
    def speedup(self):
        self.speed += 3

    def __str__(self):
        return str(self.speed)


judy = Bike()
judy.speedup()
print(judy)
judy.speedup()
print(judy)
judy.speed = 100
print(judy)