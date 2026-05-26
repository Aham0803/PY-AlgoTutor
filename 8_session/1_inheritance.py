class transport:
    def start(self):
        return "Transport is starting"

class car(transport):
    def drive(self):
        return "car is driving"
    
mycar = car()

print(mycar.start())
print(mycar.drive())