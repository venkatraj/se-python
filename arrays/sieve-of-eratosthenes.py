def printPrimes(n):
    primes = [True for _ in range(n+1)]
    divisor = 2
    while divisor * divisor <= n:
        if primes[divisor]:
            i = 2 * divisor
            while i <= n:
                primes[i] = False
                i += divisor
        divisor += 1
    count = 2
    while count <= n:
        if primes[count]:
            print(primes.index(primes[count], count), end=" ")
        count += 1


def main():
    printPrimes(120)


if __name__ == '__main__':
    main()
