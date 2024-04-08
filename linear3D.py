class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Unsupported operand type for -: 'Point3D' and '{}'".format(type(other)))
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

def get_point():
    s = input('Enter point coordinates (x, y, z): ')
    ls = s.split(',')
    x,y,z = int(ls[0]), int(ls[1]), int(ls[2])
    return Point3D(x, y, z)

def is_linerly_dependent(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    return v1 == v2

def main():
    s = ''
    while not s or s[0] in ('y', 'Y'):
        p1 = get_point()
        p2 = get_point()
        p3 = get_point()
        if is_linerly_dependent(p1, p2, p3):
            print('Points are linerly dependent')
        else:
            print('Points are not linerly dependent')
        s = input("Do you want to continue? (yes/no): ")

if __name__ == '__main__':
    main()