import math
def filter_prime(numbers):
    primes = []
    for n in numbers:
        if n>1 and all(n%i != 0 for i in range(2, int(n**0.5)+1)):
            primes.append(n)
    return primes
    
numbers_list = [1,2,3,45,33,23,66554,4356, 459001]
print(filter_prime(numbers_list))
        