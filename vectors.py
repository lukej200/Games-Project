# The Vector class
class Vector:
    # Initialiser
    def __init__(self, p=(0, 0)):
        self.x = p[0]
        self.y = p[1]

    # Returns a string representation of the vector
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Tests the equality of this vector and another
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Tests the inequality of this vector and another
    def __ne__(self, other):
        return not self.__eq__(other)

        # Returns a tuple with the point corresponding to the vector

    def getP(self):
        return (self.x, self.y)

    # Returns a copy of the vector
    def copy(self):
        v = Vector()
        v.x = self.x
        v.y = self.y
        return v

    # Multiplies the vector by a scalar
    def mult(self, k):
        self.x = self.x * k
        self.y = self.y * k
        return self

    # Divides the vector by a scalar
    def div(self, k):
        self.x = self.x / (1. * k)
        self.y = self.y / (1. * k)
        return self

    # Normalizes the vector
    def normalise(self):
        pass

    # Returns a normalized version of the vector
    def getNormalised(self):
        pass

    # Adds another vector to this vector
    def add(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # Subtracts another vector from this vector
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    # Returns the zero vector
    def zero(self):
        self.x = 0
        self.y = 0
        return self

    # Negates the vector (makes it point in the opposite direction)
    def negate(self):
        self.x = -self.x
        self.y = -self.y
        return self

    # Returns the dot product of this vector with another one
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Returns the length of the vector
    def length(self):
        return math.sqrt(self.lengthSquared())

    # Returns the squared length of the vector
    def lengthSquared(self):
        return self.x ** 2 + self.y ** 2

    # Reflect this vector on a normal
    def reflect(self, normal):
        n = normal.copy()
        n.mult(2 * self.dot(normal))
        self.sub(n)
        return self

    # Returns the angle between this vector and another one
    # You will need to use the arccosine function:
    # acos in the math library
    def angle(self, other):
        pass

