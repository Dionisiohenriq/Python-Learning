# lists are used mostly for data ordenation they differ from sets cause lists can repeat values
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)
print(primes)

primes.reverse()
primes.reverse()
print(primes[: -1]) # this gets the numbers from 0 to index x of the list

example = [123, True, "Alpha", 1.732, [64, False]] 

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

print(numbers + letters)  #order matters
print(letters + numbers)



