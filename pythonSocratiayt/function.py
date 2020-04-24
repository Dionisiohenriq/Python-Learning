dir()

def f():
	pass


def ping():
	return "Ping!"

print(ping())

x = ping()

print(x)

dir()
import math as m
def volume(r):
	"""Returns the volume of a sphere with radius r."""
	v = (4.0/3.0) * m.pi * r**3
	return v

print(volume(2))