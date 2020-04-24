# sets are like groups of data, that you can compare

example = set()

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens)) # don't change the original set
print(odds.intersection(primes)) # verify if the numbers in one set are contained in another
print(2 in primes) # verify if an element is in one set
print(9 not in primes) # verify if an element is not in a set

