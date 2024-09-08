from random import randint
from random import uniform as randfloat


class Point:  # test literally everything in this module
    total_points = 0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        Point.total_points += 1

# converters
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        if self.x > 0 and self.y > 0:
            return True
        else:
            return False

    def __int__(self):  # work on this to take false points
        return (self.x * 100) + self.y

    def __float__(self):  # same for this
        return self.x + (self.y / 100)

    def __neg__(self):
        return Point(-self.x, -self.y)

# operations DON'T REDEFINE
    def __add__(self, other):
        return Point(x=self.x + other.x, y=self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(x=self.x - other.x, y=self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Point(x=self.x * other.x, y=self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __truediv__(self, other):
        return Point(x=self.x / other.x, y=self.y / other.y)

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def __pow__(self, power):
        if isinstance(power, Point):
            return Point(x=self.x ** power.x, y=self.y ** power.y)
        return Point(x=self.x ** power, y=self.y ** power)

    def __ipow__(self, other):
        self.x **= other.x
        self.y **= other.y
        return self

# comparators
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self.x != other.x and self.y != other.y:
            return True
        return False

    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False

    def __le__(self, other):
        if self.x <= other.x and self.y <= other.y:
            return True
        return False

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        return False

    def __ge__(self, other):
        if self.x >= other.x and self.y >= other.y:
            return True
        return False

# other dunder s
    def __del__(self):
        Point.total_points -= 1

    def __getitem__(self, index):
        index = 0 if index == "x" else index
        index = 1 if index == "y" else index
        cords = [self.x, self.y]
        return cords[index]

    def __iter__(self):
        return iter((self.x, self.y))

    def __hash__(self):
        return hash((self.x, self.y))

    def __contains__(self, item):
        cords = [self.x, self.y]
        return item in cords

    def __reversed__(self):
        return Point(self.y, self.x)

# REDEFINES
    def move(self, add_x, add_y):
        self.x += add_x
        self.y += add_y
        return self

# CLASS
    @classmethod
    def help(cls):  # work on this
        print("")

# STATICS

    @staticmethod
    def average(*args):
        tot = Point(0, 0)
        n_args = len(args)

        for arg in args:
            if isinstance(arg, Point):
                tot.x += arg.x
                tot.y += arg.y
            else:
                exit('"media" func took a non Point as an arg')

        return Point(tot.x / n_args, tot.y / n_args)

# distances DON'T REDEFINE
    @staticmethod
    def distance_between(point_1, point_2):  #
        return (float(point_1.x - point_2.x) ** 2.0 +
                float(point_1.y - point_2.y) ** 2.0) ** 0.5

    @staticmethod
    def distance_x(point_1, point_2):
        return abs(point_1.x - point_2.x)

    @staticmethod
    def distance_y(point_1, point_2):
        return abs(point_1.y - point_2.y)

    @staticmethod
    def distance(point, original_pnt):  # this return a Point
        return point - original_pnt

    @staticmethod
    def slope(point_1, point_2):
        slope = (point_2.y - point_1.y) / (point_2.x - point_1.x)
        return slope

    @staticmethod
    def algebraic_exp(point_1, point_2):  # this is useless
        # no idea why I added this
        slope = Point.slope(point_1, point_2)
        parte_num = point_1.y - point_1.x * slope
        if parte_num > 0:
            parte_num = "+ " + str(parte_num)
        elif parte_num == 0:
            parte_num = ""
        elif parte_num < 0:
            parte_num = f"- {abs(parte_num)}"
        return f"{slope}x {parte_num}"

    @staticmethod
    def rand_point(min_n=0, max_n=100, floats: bool = False):
        if floats:
            return Point(randfloat(min_n, max_n), randfloat(min_n, max_n))
        else:
            return Point(randint(min_n, max_n), randint(min_n, max_n))


class Line:
    total_lines = 0

    def __init__(self, p_1: Point, p_2: Point):
        self.p_1 = p_1
        self.p_2 = p_2
        self.length = Point.distance_between(self.p_1, self.p_2)
        Line.total_lines += 1

    def __str__(self):
        return f"({self.p_1}; {self.p_2})"

    def __int__(self):
        return (int(self.p_1) * 1000) + int(self.p_2)

    def __float__(self):
        return int(self.p_1) + (int(self.p_2) / 1000)

    def __bool__(self):
        if bool(self.p_1) and bool(self.p_2):
            return True
        return False

    def __neg__(self):
        return Line(-self.p_1, -self.p_2)

# operations DON'T REDEFINE
    def __add__(self, other):
        return Line(self.p_1 + other.p_1, self.p_2 + other.p_2)

    def __iadd__(self, other):
        self.p_1 += other.p_1
        self.p_2 += other.p_2
        return self

    def __sub__(self, other):
        return Line(self.p_1 - other.p_1, self.p_2 - other.p_2)

    def __isub__(self, other):
        self.p_1 -= other.p_1
        self.p_2 -= other.p_2
        return self

    def __mul__(self, other):
        return Line(self.p_1 * other.p_1, self.p_2 * other.p_2)

    def __imul__(self, other):
        self.p_1 *= other.p_1
        self.p_2 *= other.p_2
        return self

    def __truediv__(self, other):
        return Line(self.p_1 / other.p_1, self.p_2 / other.p_2)

    def __itruediv__(self, other):
        self.p_1 /= other.p_1
        self.p_2 /= other.p_2
        return self

    def __pow__(self, other):
        return Line(self.p_1 ** other.p_1, self.p_2 ** other.p_2)

    def __ipow__(self, other):
        self.p_1 **= other.p_1
        self.p_2 **= other.p_2
        return self

# comparators
    def __eq__(self, other):
        if self.p_1 == other.p_1 and self.p_2 == other.p_2:
            return True
        return False

    def __ne__(self, other):
        if self.p_1 != other.p_1 and self.p_2 != other.p_2:
            return True
        return False

    def __lt__(self, other):
        if self.p_1 < other.p_1 and self.p_2 < other.p_2:
            return True
        return False

    def __le__(self, other):
        if self.p_1 <= other.p_1 and self.p_2 <= other.p_2:
            return True
        return False

    def __gt__(self, other):
        if self.p_1 > other.p_1 and self.p_2 > other.p_2:
            return True
        return False

    def __ge__(self, other):
        if self.p_1 >= other.p_1 and self.p_2 >= other.p_2:
            return True
        return False

    # other dunder s
    def __del__(self):
        Line.total_lines -= 1

    def __getitem__(self, index):
        pnts = [self.p_1, self.p_2]
        return pnts[index]

    def __iter__(self):
        return iter((self.p_1, self.p_2))

    def __hash__(self):
        return hash((self.p_1, self.p_2))

    def __contains__(self, item):
        points = [self.p_1, self.p_2]
        return item in points

    def __reversed__(self):
        return Line(self.p_2, self.p_1)

# STATIC

    @staticmethod
    def average(*lines):
        ps1 = []
        ps2 = []
        for line_ in lines:
            ps1.append(line_.p_1)
            ps2.append(line_.p_2)

        return Line(Point.average(*ps1), Point.average(*ps2))

    @staticmethod
    def avr_length(*lines):
        tot = 0.0
        for line in lines:
            tot += line.lenght

        return tot / len(lines)