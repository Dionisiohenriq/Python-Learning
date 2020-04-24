import math
print(math.pi)

def volume(r):
    """Function that calculate a sphere volume r."""
    v = (4.0/3.0) * math.pi * r ** 3
    return v

print(volume(2))

def triangle_area(b, h):
    """Returns the area of a triangle with base b and height t."""
    return 0.5 * b * h

print(triangle_area(3, 6))

def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 2.54 * 12
    return inches_to_cm + feet_to_cm

print(cm(feet= 5))
print(cm(inches= 70))
print(cm(feet= 5, inches= 8))
print(cm(inches= 8, feet= 5))

def g(t, x = 0):
    return t + x

print(g(5))

print(g(7, x = 5))
print(g(5, 5))