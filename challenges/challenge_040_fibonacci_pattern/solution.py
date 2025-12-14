# Challenge 040: Fibonacci Series Pattern (N Rows)

def main():
    n = int(input("Enter number of rows: "))

    a, b = 1, 1
    count = 1

    for i in range(1, n + 1):
        for j in range(i):
            print(a, end=" ")
            a, b = b, a + b
        print()


if __name__ == "__main__":
    main()
