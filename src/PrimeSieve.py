from bitarray import bitarray
from math import isqrt


class PrimeSieve:
    '''

    Implements the sieve of Eratosthenes for finding primes less than N

    The sieve runs when the PrimeSieve is instantiated

    Methods:
        primes() - returns a generator yielding the primes in the sieve
        countPrimes() - returns the number of primes in the sieve

    '''

    def __init__(self, N):
        self.N = N

        self.sieve = bitarray(N // 2)
        self.sieve.setall(1)

        for div in range(3, isqrt(N) + 1, 2):
            if self.sieve[div // 2]:
                for x in range(div ** 2, N, 2 * div):
                    self.sieve[x // 2] = 0

    def primes(self):
        yield 2

        for x in range(3, self.N, 2):
            if self.sieve[x // 2]:
                yield x

    def countPrimes(self):
        return sum(1 for _ in self.primes())
