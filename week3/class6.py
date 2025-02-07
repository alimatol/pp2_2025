class FilterPrime:
    def is_prime(self, n):
        return n>1 and all(n%i != 0 for i in range(2, int(n**0.5)+1))

    def filter(self, primes):
        return list(filter(self.is_prime, primes))
    
list_num = [2,3, 434,34, 2021.341,13, 17]
filtered = FilterPrime()

print(filtered.filter(list_num))