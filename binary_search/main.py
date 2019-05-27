from binary_search import binary_search, binary_search_recursion


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = binary_search(5, primes)
    print(result)
    result = binary_search(79, primes)
    print(result)
    result = binary_search_recursion(5, primes, 0, len(primes))
    print(result)
    result = binary_search_recursion(79, primes, 0, len(primes))
    print(result)


if __name__ == '__main__':
    main()
