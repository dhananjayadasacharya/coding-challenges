def main():
    n = int(input("Enter number of terms: "))

    series = [1]
    count = 0   # to count +4 steps

    for i in range(1, n):
        if count < 3:
            series.append(series[-1] + 4)
            count += 1
        else:
            series.append(series[-1] + 8)
            count = 0

    print(",".join(str(x) for x in series))


if __name__ == "__main__":
    main()
