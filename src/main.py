from PrimeSieve import PrimeSieve
from pprint import pprint


def main():
    print('Hello World!', end='\n\n')

    print('Day 2 - Prime Sieve', end='\n\n')
    N = 200
    print(f'Primes less than {N:,}:')
    pprint(list(PrimeSieve(N).primes()), compact=True)
    N = 1_000_000
    count = PrimeSieve(N).countPrimes()
    print(f'Number of primes less than {N:,}: {count:,}')


if __name__ == '__main__':
    main()
