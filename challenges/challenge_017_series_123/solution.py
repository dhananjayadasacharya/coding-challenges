def main():
    n = int(input("Enter N: "))
    series = [str(i) for i in range(1, n + 1)]
    print(",".join(series))

if __name__ == "__main__":
    main()
