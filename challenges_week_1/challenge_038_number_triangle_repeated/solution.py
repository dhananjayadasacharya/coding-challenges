# Challenge 038: Printing Number Increasing Pattern (N Rows, repeated digit)

def main():
    n = int(input("Enter number of rows: "))

    for i in range(1, n + 1):
        print(str(i) * i)


if __name__ == "__main__":
    main()
