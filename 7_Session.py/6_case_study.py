# create a class for vehicles which stores information like vehicle_name , vehicle_type , top_speed etc. add few objects to it

class vehical:
    def __init__(self , name , model , year , top_speed):
        self.name = name
        self.model = model
        self.year = year
        self.top_speed = top_speed

vehicle1 = vehical("BMW" , "X5" , 2020 , 250)
vehicle1 = vehical("Audi" , "07" , 2021 , 260)
vehicle1 = vehical("Mercedes" , "X0" , 2024 , 260)

print(f" Vehicle Name : {vehicle1.name} , Model : {vehicle1.model} , year : {vehicle1.year}")