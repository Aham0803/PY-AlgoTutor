# create an "Greeter" class whiich greets users as GoodMoring , good evening , good night by the username

from datetime import datetime

class Greeter:
    def __init__(self,username):
        self.username = username

    def greet(self):
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            greeting = "Good Morning"
        elif 12 <= current_hour < 18:
            greeting = "Good Evening"
        else:
            greeting = "Good Night"

        return f"{greeting} , {self.username}"

if __name__ == "__main__":
    greeter = Greeter("Gaurab")
    print(greeter.greet())