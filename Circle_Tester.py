import math


# create class
class Circle:
    # initialization
    def __init__(self, radius):
        self.radius = radius

    # methods
    def calculate_diameter(self):
        return f'Diameter: {self.radius * 2}'

    def calculate_circumference(self):
        return f'Circumference: {self.radius * 2 * math.pi}'

    def calculate_area(self):
        return f'Area: {math.pi * (self.radius ** 2)}'

    def grow(self):
        while True:
            grow = input("Would you like your circle to grow? (y/n)\n> ")
            if grow == 'y':
                self.radius *= 2
                print('Stand by while your circle magically grows...')
                print(self.calculate_diameter())
                print(self.calculate_circumference())
                print(self.calculate_area())
            else:
                print('See yah')
                break


print("Welcome to the Circle Tester!")

# enter input for radius
radius = float(input("Enter the radius of a circle:\n> "))

# create Circle using class
circle = Circle(radius)

# display initial results
print(circle.calculate_diameter())
print(circle.calculate_circumference())
print(circle.calculate_area())

# ask user if they want circle to grow
circle.grow()
