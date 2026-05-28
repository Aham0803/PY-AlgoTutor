#vehicle class defines a common interface with "start_engine"method. the "car" and
#"motorcyle" class overides this method to provide their specific implementation. the "initiate_engine" function accepts objects of diffrent types and invokes the correct "start_engine" method

class vehicle:
    def start_engine(self):
        print("Starting the engine...")
class Car(vehicle):
    def start_engine(self):
        print("Starting the car engine")
class Motorcycle(vehicle):
    def start_engine(self):
        print("starting the motorcycle engine...")

def initiate_engine(Vehicle):
    return Vehicle.start_engine()

car = Car()
motorcycle = Motorcycle()

initiate_engine(car)
initiate_engine(motorcycle)