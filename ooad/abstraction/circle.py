class Circle:
    def __init__(self):
        self.radius = 0
        self.pi = 3.142
    
    def __init__(self, r):
        self.radius = r
        self.pi = 3.142
    
    def area(self):
        return self.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * self.pi * self.radius
    
def main():
    circle = Circle(5)
    print("Area: {:.2f}".format(circle.area()))
    print("Perimeter: {:.2f}".format(circle.perimeter()))

if __name__ == "__main__":
    main()