class Polygon:
    pi = 3.14159
    @ staticmethod
    def get_area(factors, sides, cfacts):
        data = []
        for name in sides:
            x = float(input(f"Enter the {name} of the polygon: "))
            data.append(x)
        prod = 1
        for i in factors:
            prod *= data[i-1]
        for i in cfacts:
            prod *= i
        return prod

class Square(Polygon):
    def __init__(self):
        self.area = Polygon.get_area([1,1], ['side'], [])

class Rectangle(Polygon):
    def __init__(self):
        self.area = Polygon.get_area([1,2], ['length', 'breadth'], [])

class Sphere(Polygon):
    def __init__(self):
        self.area = Polygon.get_area([1,1,1], ['radius'], [4/3, Polygon.pi])
if __name__ == '__main__':
    s = Square()
    print(f"Area of square: {s.area}")
    r = Rectangle()
    print(f"Area of rectangle: {r.area}")
    sp = Sphere()
    print(f"Area of sphere: {sp.area}")