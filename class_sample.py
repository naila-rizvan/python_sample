# Find area of different shapes

class Area:

    def circle(self):
        pi = 3.14
        radius = float(input("Enter the radius of circle: "))
        area = pi * pow(radius,2)
        return area

    def rectangle(self):
        length = float(input("Enter the length of rectangle: "))
        breadth = float(input("Enter the breadth of rectangle: "))
        area = length * breadth
        return area

    def square(self):
        side = float(input("Enter the side of square: "))
        area = side**2
        return area


area = Area()

print("Choose a shape to find area")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1: print("Area of circle: " + str(area.circle()))
    case 2: print("Area of rectangle: " + str(area.rectangle()))
    case 3: print("Area of square: " + str(area.square()))
    case _: print("Invalid Choice")

