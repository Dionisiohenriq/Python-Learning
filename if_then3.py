#Scalene triangle: all sides have different lengths
#Isoceles triangle: two sides of the same lengths
#Equilateral triangle: all sides are equal.

a = int(input("Enter the length of a side: "))
b = int(input("Enter the length of b side: "))
c = int(input("Enter the length of c side: "))

if a + b > c and a + c > b and b + c > a:
	if a != b and b != c and a != c:
		print("Scalene triangle")
	elif a == b and b == c:
		print("Equilateral triangle")
	else:
		print("Isoceles triangle")