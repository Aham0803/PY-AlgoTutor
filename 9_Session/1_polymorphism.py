class DataEngineering:
    def Course(self):
        print("Data Enginnering Course")

class Python(DataEngineering): # child class
    def Course(self): #method overriding
        print("Python Course")

class Data(DataEngineering):#child class
    def Course(self):
        print("Data Course")

for x in [Python() , Data()]: #Polymorphism
    x.Course() #method calling

    