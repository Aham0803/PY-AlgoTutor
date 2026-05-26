#polymorphism

class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return "Area of square is side^2"
    
class Circle(Shape):
    def area(self):
        return "ar of circle is pi*r^2"

shape = [Shape() , Square() , Circle()]
for s in shape:
    print(s.area())