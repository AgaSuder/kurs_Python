#!/usr/bin/python3
import math
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):        # return string "Vector(x, y, z)"
        print("Vector(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")")
    def __eq__(self, other):   # v == w
        return self.x == other.x and self.y == other.y and self.z == other.z
    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):   # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):   # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):  # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):   # return the cross product (Vector)
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    def length(self):    # the length of the vector
        return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))
    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

def find_axis(v1, v2):
    if v1.cross(v2) == Vector(0, 0, 0):
        raise ValueError("v1 and v2 are parallel")
    return Vector(v1.y * v2.z - v2.y * v1.z, -(v1.x * v2.z - v2.x * v1.z), v1.x * v2.y - v1.y * v2.x)
    
# Exemplary tests. Change values in your tests.
v = Vector(3, 1, -3)
w = Vector(5, -2, -2)
assert v != w
assert v + w == Vector(8, -1, -5)
assert v - w == Vector(-2, 3, -1)
assert v * w == 19
assert v.cross(w) == Vector(-8, -9, -11)
assert v.length() == math.sqrt(19)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")

v1 = Vector(2, 3, 4)
v2 = Vector(1, 2, 3)
v3 = find_axis(v1,v2)
input()