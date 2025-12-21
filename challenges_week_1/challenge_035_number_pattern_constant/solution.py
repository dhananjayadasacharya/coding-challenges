# Challenge 035: Printing Number Pattern (N Rows, constant digit)

def main():
    n = int(input("Enter number of rows: "))

    for i in range(1, n + 1):
        print(str(i) * 5)


if __name__ == "__main__":
    main()
