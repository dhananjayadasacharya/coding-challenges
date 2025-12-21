def main():
    n = int(input("Enter N: "))
    series = []
    val = 1
    for i in range(1, n + 1):
        series.append(str(val))
        val += i
    print(",".join(series))

if __name__ == "__main__":
    main()
