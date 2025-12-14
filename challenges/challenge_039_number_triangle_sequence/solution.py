# Challenge 039: Printing Number Increasing Pattern (N Rows, 1..i)

def main():
    n = int(input("Enter number of rows: "))

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


if __name__ == "__main__":
    main()
