class user:
    def __init__(self,name):
        self.__name = name # private attribute
    def get_name(self):
        return self.__name
    
user1 = user("Gaurav")
print(user1.get_name()) #Accessing private attribute through a public method