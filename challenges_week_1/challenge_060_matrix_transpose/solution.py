# Challenge 060: 2D Arrays (Matrix and Transpose)

def main():
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input("Enter element: ")))
        matrix.append(row)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("Transpose Matrix:")
    for j in range(c):
        for i in range(r):
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
