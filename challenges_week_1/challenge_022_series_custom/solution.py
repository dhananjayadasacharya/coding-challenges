def main():
    n = int(input("Enter number of terms: "))

    series = [1, 4, 7]

    for i in range(3, n):
        series.append(series[i-1] + series[i-2] + series[i-3])

    print(",".join(str(x) for x in series[:n]))

if __name__ == "__main__":
    main()
