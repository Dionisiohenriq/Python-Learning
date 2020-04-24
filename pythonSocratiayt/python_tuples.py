# list example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

print(len(perfect_squares))
print(len(prime_numbers))

# for p in prime_numbers:
#     print("# Primes = ", p)
# for s in perfect_squares:
#     print("# Perfect_squares = ", s)


# print("# List Methods")
# print(dir(prime_numbers))
# print(80 * "-")
# print("# Tuples Methods")
# print(dir(perfect_squares))

import sys
# print(dir(sys))

# print(help(sys.getsizeof))

# print("# Sizeof list = ", sys.getsizeof(prime_numbers))
# print('# Size of tuple = ', sys.getsizeof(perfect_squares))

#print(help('modules'))
test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3

print(type(test1))
print(test3)

survey = (21, "switzerland", False)
age, country, knows_python = survey

print(age)
print(country)
print(knows_python)