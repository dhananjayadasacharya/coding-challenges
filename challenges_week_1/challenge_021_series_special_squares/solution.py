def main():
    n = int(input("Enter N: "))
    primes = []
    for num in range(2, 100):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
            if len(primes) == n:
                break
    series = [str(p ** 2) for p in primes]
    print(",".join(series))

if __name__ == "__main__":
    main()
