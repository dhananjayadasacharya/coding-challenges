# Challenge 041: Perfect Squares with Alternating Signs (N Rows)

def main():
    n = int(input("Enter number of rows: "))

    num = 1
    sign = 1

    for i in range(1, n + 1):
        for j in range(i):
            value = (num ** 2) * sign
            print(value, end=" ")
            sign *= -1
            num += 1
        print()


if __name__ == "__main__":
    main()
