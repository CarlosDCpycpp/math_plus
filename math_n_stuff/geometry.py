from random import randint
from random import uniform as randfloat
import math

from important_nums import pi
import utils

import utils


class Point:
    """A 2-dimensional point."""

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

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))

    def __contains__(self, item):
        cords = [self.x, self.y]
        return item in cords

    def __reversed__(self):
        return Point(self.y, self.x)

# REDEFINES
    def move(self, add_x, add_y):
        """Redefines the point by adding the arguments passed to the respective coordinates."""
        self.x = add_x
        self.y = add_y
        return self

# STATICS

    @staticmethod
    def average(*args):
        """Calculates the average point of the points that are passed as *args."""
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
        """Calculates the average distance between the points passed as *args."""
        return (float(point_1.x - point_2.x) ** 2.0 +
                float(point_1.y - point_2.y) ** 2.0) ** 0.5

    @staticmethod
    def distance_x(point_1, point_2):
        """Calculates the distance between the y of the points passed as *args."""
        return abs(point_1.x - point_2.x)

    @staticmethod
    def distance_y(point_1, point_2):
        """Calculates the distance between the x of the points passed as *args."""
        return abs(point_1.y - point_2.y)

    @staticmethod
    def distance_point(point, original_pnt):  # this return a Point
        """Calculates the distance between the x of the points passed as *args."""
        return point - original_pnt

    @staticmethod
    def slope(point_1, point_2):
        """Calculates the slope of 2 points that are passed as arguments."""
        slope = (point_2.y - point_1.y) / (point_2.x - point_1.x)
        return slope

    @staticmethod
    def algebraic_exp(point_1, point_2):  # this is useless
        # no idea why I added this
        """Returns a string with the algebraic expression of the linear function
        that the two points that are passed as *args compose.
        WARNING:
            This is limited to LINEAR FUNCTIONS."""
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
    def rand(min_n=0, max_n=100, float_: bool = False):
        """Creates a random point.
        Arguments can be passed to indicate some restrictions, those are, consecutively:
        min_n, max_n, float_.
        The first two determine the limits of the random point's position,
        the third determines if the x and y can be floats."""
        if float_:
            return Point(randfloat(min_n, max_n), randfloat(min_n, max_n))
        else:
            return Point(randint(min_n, max_n), randint(min_n, max_n))


class Line:
    """A 2-dimensional line."""

    total_lines = 0

    def __init__(self, p1: Point = Point(), p2: Point = Point(0, 1)):
        self.p1 = p1
        self.p2 = p2
        self.length = Point.distance_between(self.p1, self.p2)
        Line.total_lines += 1

    def __str__(self):
        return f"({self.p1}; {self.p2})"

    def __bool__(self):
        if bool(self.p1) and bool(self.p2):
            return True
        return False

    def __neg__(self):
        return Line(-self.p1, -self.p2)

# operations DON'T REDEFINE
    def __add__(self, other):
        return Line(self.p1 + other.p1, self.p2 + other.p2)

    def __iadd__(self, other):
        self.p1 += other.p1
        self.p2 += other.p2
        return self

    def __sub__(self, other):
        return Line(self.p1 - other.p1, self.p2 - other.p2)

    def __isub__(self, other):
        self.p1 -= other.p1
        self.p2 -= other.p2
        return self

    def __mul__(self, other):
        return Line(self.p1 * other.p1, self.p2 * other.p2)

    def __imul__(self, other):
        self.p1 *= other.p1
        self.p2 *= other.p2
        return self

    def __truediv__(self, other):
        return Line(self.p1 / other.p1, self.p2 / other.p2)

    def __itruediv__(self, other):
        self.p1 /= other.p1
        self.p2 /= other.p2
        return self

    def __pow__(self, other):
        return Line(self.p1 ** other.p1, self.p2 ** other.p2)

    def __ipow__(self, other):
        self.p1 **= other.p1
        self.p2 **= other.p2
        return self

# comparators
    def __eq__(self, other):
        if self.p1 == other.p1 and self.p2 == other.p2:
            return True
        return False

    def __ne__(self, other):
        if self.p1 != other.p1 and self.p2 != other.p2:
            return True
        return False

    def __lt__(self, other):
        if self.p1 < other.p1 and self.p2 < other.p2:
            return True
        return False

    def __le__(self, other):
        if self.p1 <= other.p1 and self.p2 <= other.p2:
            return True
        return False

    def __gt__(self, other):
        if self.p1 > other.p1 and self.p2 > other.p2:
            return True
        return False

    def __ge__(self, other):
        if self.p1 >= other.p1 and self.p2 >= other.p2:
            return True
        return False

    # other dunder s
    def __del__(self):
        Line.total_lines -= 1

    def __hash__(self):
        return hash((self.p1, self.p2))

    def __getitem__(self, index):
        pnts = [self.p1, self.p2]
        return pnts[index]

    def __iter__(self):
        return iter((self.p1, self.p2))

    def __contains__(self, item):
        points = [self.p1, self.p2]
        return item in points

    def __reversed__(self):
        return Line(self.p2, self.p1)

# STATIC

    @staticmethod
    def average(*lines):
        ps1 = []
        ps2 = []
        for line_ in lines:
            ps1.append(line_.p1)
            ps2.append(line_.p2)

        return Line(Point.average(*ps1), Point.average(*ps2))

    @staticmethod
    def avr_length(*lines):
        tot = 0.0
        for line in lines:
            tot += line.lenght

        return tot / len(lines)

    @staticmethod
    def rand(min_=-100, max_=100, float_=False):
        return Line(Point.rand(min_, max_, float_), Point.rand(min_, max_, float_))


class Vector(Line):
    total_vectors = 0

    def __init__(self, line, strength=1.0):
        Vector.total_vectors += 1

        if isinstance(line, Line):
            p1 = line.p1
            p2 = line.p2
        elif isinstance(line, list):
            p1 = line[0]
            p2 = line[1]
        else:
            raise ValueError

        super().__init__(p1, p2)
        self.line = Line(p1, p2)
        self.strength = strength

        self.shift = self.p2 - self.p1

    def __str__(self):
        return str(self.line) + f"; Strength: {self.strength}"

    def __neg__(self):
        return Vector(-self.line, strength=-self.strength)

    def __del__(self):
        Vector.total_vectors -= 1

    def __call__(self, other, sum_=True):
        if sum_:
            return other + self
        else:
            return other - self

# reverse operating
    # I'm going to just leave it with only radd and rsub
    # since it's what makes the most sense

    def __radd__(self, other):
        if isinstance(other, Polygon):
            z = []
            for pnt in other.points:
                z.append(pnt + self.shift)
            return Polygon(z)
        if isinstance(other, Circle):
            center = other.center + self.shift
            edge = other.edge + self.shift
            return Circle(center=center, edge=edge)
        if isinstance(other, Point):
            return other + self.shift
        if isinstance(other, Line):
            return Line(p1=other.p1+self.shift, p2=other.p2+self.shift)

    def __rsub__(self, other):
        return other + -self

# other dunder s

    def __hash__(self):
        return hash((self.line, self.strength))

# STATICS

    @staticmethod
    def rand_(min_=-100, max_=100,
              min_strength=-50, max_strength=50,
              line_float=False, strength_float=False):
        l_ = Line.rand(min_, max_, line_float)
        if strength_float:
            s = randfloat(min_strength, max_strength)
        else:
            s = randint(min_strength, max_strength)
        return Vector(l_, s)


class Polygon:
    total_polygons = 0

    def __init__(self, points):

        Polygon.total_polygons += 1

        self.points = utils.filter_list(points)

        self.lines = []
        self.lines.append(Line(points[-1], points[0]))
        for point in points:
            if point == self.points[-1]:
                continue
            nx_p = self.points[self.points.index(point) + 1]
            self.lines.append(Line(point, nx_p))

        self.perimeter = 0
        for line in self.lines:
            self.perimeter += line.length

        self.n_lines = len(self.lines)

        # angles
        self.sum_inner_angles = (self.n_lines - 2) * 180

        self.angles = self.helper_calculate_angles()

        self.area = 0.0  # I haven't learnt this yet so GPT made it
        for i in range(self.n_lines):
            x1, y1 = self.points[i].x, self.points[i].y
            x2, y2 = self.points[(i + 1) % self.n_lines].x, self.points[(i + 1) % self.n_lines].y
            self.area += x1 * y2 - x2 * y1
        self.area = abs(self.area) / 2.0

        # regular
        z = []
        for line in self.lines:
            z.append(line.length)

        if utils.all_elements_same(self.angles) and utils.all_elements_same(z):
            self.is_regular = True
        else:
            self.is_regular = False

        # type_
        self.type_ = self.helper_determine_type_()

# HELPERS
    def helper_calculate_angles(self):  # GPT did this
        angles = []
        for i in range(self.n_lines):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % self.n_lines]
            p3 = self.points[(i + 2) % self.n_lines]

            # Vectors
            v1 = (p2.x - p1.x, p2.y - p1.y)
            v2 = (p3.x - p2.x, p3.y - p2.y)

            # Dot product and magnitudes
            dot_product = v1[0] * v2[0] + v1[1] * v2[1]
            mag_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
            mag_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)

            # Angle in radians
            angle_rad = math.acos(dot_product / (mag_v1 * mag_v2))
            # Convert to degrees
            angle_deg = math.degrees(angle_rad)
            angles.append(angle_deg)

        return angles

    def helper_determine_type_(self):  # up to 12
        polygon_names = {
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon",
            11: "Hendecagon",
            12: "Dodecagon"
        }

        polygon_name = polygon_names.get(self.n_lines, "Unknown")

        if self.n_lines == 3:
            if all(math.isclose(angle, 60, abs_tol=1e-6) for angle in self.angles):
                type_ = ["Triangle", "Equilateral"]
            elif any(math.isclose(angle, 90, abs_tol=1e-6) for angle in self.angles):
                type_ = ["Triangle", "Right"]
            elif len(set(self.angles)) == 2:
                type_ = ["Triangle", "Isosceles"]
            else:
                type_ = ["Triangle", "Scalene"]

        elif self.n_lines == 4:
            if any(math.isclose(self.angles[i], 90, abs_tol=1e-6) for i in range(4)):
                if utils.all_elements_same(self.angles) and self.angles[0] == 90:
                    type_ = "Rectangle"
                else:
                    type_ = "Right Trapezoid"
            else:
                if utils.all_elements_same(self.angles[1:3]) and len(set(self.angles)) == 3:
                    type_ = "Isosceles Trapezoid"
                else:
                    type_ = "Trapezoid"

        elif self.is_regular:
            if self.n_lines == 4:
                if utils.all_elements_same(self.angles) and self.angles[0] == 90:
                    type_ = "Square"
                else:
                    type_ = "Rhombus"
            else:
                type_ = polygon_name

        else:
            type_ = polygon_name

        return type_

# converters
    def __str__(self):
        str_ = ""
        for i in self.points:
            str_ += f"{i}; "
        str_ = str_[:-2]
        return str_

    def __bool__(self):
        for point in self.points:
            if not point:
                return False
        return True

    def __neg__(self):
        n_pnts = []
        for pnt in self.points:
            n_pnts.append(-pnt)
        return Polygon(n_pnts)

# operators
    pass  # add these with vectors and polygons
    pass  # vectors: apply the vector to each point
    pass  # polygons: fuse them (try at least)

# comparators
    # I'm comparing AREAS
    def __eq__(self, other):
        if self.points == other.points:
            return True
        return False

    def __ne__(self, other):
        if self.points != other.points:
            return True
        return False

    def __lt__(self, other):
        if self.area < other.area:
            return True
        return False

    def __le__(self, other):
        if self.area <= other.area:
            return True
        return False

    def __gt__(self, other):
        if self.area > other.area:
            return True
        return False

    def __ge__(self, other):
        if self.area >= other.area:
            return True
        return False

# other dunder s
    def __del__(self):
        Polygon.total_polygons -= 1

    def __getitem__(self, index_):  # type_ can be "line"
        type_ = "p"
        index = None

        if isinstance(index_, tuple):
            flag1 = False
            flag2 = False
            for i in index_:
                if isinstance(i, str):
                    type_ = i
                    flag1 = True
                elif isinstance(i, int):
                    index = i
                    flag2 = True

            if not flag1 or not flag2:
                raise IndexError

        elif isinstance(index_, int):
            index = index_
            type_ = "p"

        else:
            raise IndexError

        type_ = type_.lower()
        if type_ == "point" or type_ == "pnt" or type_ == "p":
            result = self.points[index]
        elif type_ == "line" or type_ == "ln" or type_ == "l":
            result = self.lines[index]
        else:
            raise ValueError(f"Invalid Type: {type_}")
        return result

    def __iter__(self):
        return iter(self.points)

    def __contains__(self, other):
        if isinstance(other, Point):
            return other in self.points
        elif isinstance(other, Line):
            return other in self.lines
        elif isinstance(other, int):
            cords = []
            for point in self.points:
                cords.append(point.x)
                cords.append(point.y)
            return other in cords

    def __reversed__(self):
        return Polygon(self.points[::-1])

# STATICS

    @staticmethod
    def rand(min_=-100, max_=100, min_points=3, max_points=12, float_=False):
        pnts = []
        for i in range(randint(min_points, max_points)):
            pnts.append(Point.rand(min_, max_, float_))
        return Polygon(pnts)


class Circle:
    total_circles = 0

    def __init__(self, center: Point = Point(),
                 edge: Point = Point(), radius=None):
        Circle.total_circles += 1

        self.center = center
        self.edge = edge
        if radius is None:
            self.radius = Line(center, edge)
        elif isinstance(radius, Line):
            self.radius = radius
        elif isinstance(radius, (int, float)):
            self.radius = Line(center, Point(center.x, center.y + radius))
        else:
            self.radius = Line(self.center, self.edge)

        if self.edge == Point():
            self.edge = self.radius[1]
        if self.center == Point():
            self.center = self.radius[0]

        self.diameter = self.radius.length * 2

        self.all_points = []
        for angle in range(0, 360):
            x = round(self.center.x + self.radius.length * math.cos(math.radians(angle)), 5)
            y = round(self.center.y + self.radius.length * math.sin(math.radians(angle)), 5)
            self.all_points.append(Point(x, y))

        pi = 3.1416

        # area
        self.area = pi * self.radius.length ** 2

        # perimeter
        self.circumference = 2 * pi * self.radius.length

# converters
    def __str__(self):
        return f"Center: {self.center}; Radius: {self.radius.length}"

    def __bool__(self):
        if not self.center:
            return False
        return True

    def __neg__(self):
        return Circle(-self.center, -self.edge, -self.radius)

# operators

# comparators
    def __eq__(self, other):
        if isinstance(other, Circle):
            if other.center == self.center and other.radius == self.radius:
                return True
            return False
        return False

    def __ne__(self, other):
        if other == self:
            return False
        return True

    def __le__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area <= other.area:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area < other.area:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area >= other.area:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, (Polygon, Circle)):
            if self.area > other.area:
                return True
        return False

# other dunder s
    def __del__(self):
        Circle.total_circles -= 1

    def __getitem__(self, index):
        if index == 360:
            index = 0
        if index < 0:
            index += 360
        return self.all_points[index]

    def __iter__(self):
        return iter(self.all_points)

    def __contains__(self, other):
        if isinstance(other, Point):
            if other in self.all_points:
                return True
            return False
        if isinstance(other, Line):
            flag1 = False
            flag2 = False
            for i in other:
                if i == self.center:
                    flag1 = True
                elif i in self.all_points:
                    flag2 = True
            if flag1 and flag2:
                return True
            return False

# STATICS

    @staticmethod
    def rand(min_=-100, max_=100, float_=False, radius_int=False):
        center = Point.rand(min_, max_, float_)
        if radius_int:
            if float_:
                radius = Line(center, Point.rand())
        else:
            radius = Line(center, Point.rand())
        edge = Point(radius[1][0], radius[1][0])

        return Circle(center=center, radius=radius, edge=edge)


class FractionCircle(Circle):
    def __init__(self, center: Point = Point(),
                 edge: Point = Point(), radius=None,
                 percentage: int = 50):
        super().__init__(center, edge, radius)

        self.full_circle = Circle(center, edge, radius)

        self.percentage = percentage / 100
        self.area *= self.percentage
        self.circumference *= self.percentage

        self.all_points = []
        i = round(360*self.percentage)
        for angle in range(0, i):
            x = round(self.center.x + self.radius.length * math.cos(math.radians(angle)), 5)
            y = round(self.center.y + self.radius.length * math.sin(math.radians(angle)), 5)
            self.all_points.append(Point(x, y))

    def __str__(self):
        return f"{self.full_circle}; Percentage: {self.percentage * 100}"

    def __eq__(self, other):
        if (isinstance(other, FractionCircle) and
                self.full_circle == other.full_circle and
                self.percentage == other.percentage):
            return True
        return False

    def __ne__(self, other):
        if isinstance(other, FractionCircle) and self == other:
            return False
        return True

# STATICS

    @staticmethod
    def rand_(min_=-100, max_=100, float_=False,
              perc_min=10, perc_max=90, radius_int=False):
        c = Circle.rand(min_, max_, float_)
        p = randint(perc_min, perc_max)
        return FractionCircle(center=c.center, edge=c.edge,
                              radius=c.radius, percentage=p)


class Area:
    @staticmethod
    def square(side: float or int) -> int or float:
        return side**2

    @staticmethod
    def rectangle(side1: float or int, side2: float or int) -> int or float:
        return side1*side2

    @staticmethod
    def triangle(base: float or int, height: float or int) -> int or float:
        return 0.5 * base * height

    @staticmethod
    def circle(radius: float or int) -> int or float:
        return pi * radius**2


class Volume:
    @staticmethod
    def cube(side: int or float) -> int or float:
        return side**3

    @staticmethod
    def sphere(radius: int or float) -> int or float:
        return (4/3) * pi * radius**3

    @staticmethod
    def cylinder(radius: int or float, height: int or float) -> int or float:
        return pi * radius**2 * height

    @staticmethod
    def cone(radius: int or float, height: int or float) -> int or float:
        return (1/3) * pi * radius**2 * height


class SurfaceArea:
    @staticmethod
    def sphere(radius: int or float) -> int or float:
        return 4 * pi * radius**2

    @staticmethod
    def cylinder(radius: int or float, height: int or float) -> int or float:
        return 2 * pi * radius * (radius + height)


def slope(x1, x2, y1, y2) -> float or int:
    return (y2 - y1) / (x2 - x1)


def pythagoras_t(a: int or float, b: int or float) -> int or float:
    return (a**2 + b**2) ** 0.5


if __name__ == "__main__":
    pass
