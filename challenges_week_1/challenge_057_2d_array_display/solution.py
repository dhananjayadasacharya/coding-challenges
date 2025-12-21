# Challenge 057: 2D Arrays (Display row-wise)

def main():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input("Enter element: ")))
        matrix.append(row)

    print("Matrix:")
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


if __name__ == "__main__":
    main()
