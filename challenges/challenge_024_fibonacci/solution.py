def main():
    n = int(input("Enter N: "))
    series = [1, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    print(",".join(str(x) for x in series[:n]))

if __name__ == "__main__":
    main()
