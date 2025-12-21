# Challenge 061: Multiply Two Matrices

def main():
    r1 = int(input("Enter rows of matrix 1: "))
    c1 = int(input("Enter columns of matrix 1: "))

    r2 = int(input("Enter rows of matrix 2: "))
    c2 = int(input("Enter columns of matrix 2: "))

    if c1 != r2:
        print("Matrix multiplication not possible")
    else:
        A = []
        B = []

        print("Enter elements of Matrix 1")
        for i in range(r1):
            row = []
            for j in range(c1):
                row.append(int(input()))
            A.append(row)

        print("Enter elements of Matrix 2")
        for i in range(r2):
            row = []
            for j in range(c2):
                row.append(int(input()))
            B.append(row)

        result = [[0 for _ in range(c2)] for _ in range(r1)]

        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    result[i][j] += A[i][k] * B[k][j]

        print("Resultant Matrix:")
        for row in result:
            print(row)


if __name__ == "__main__":
    main()
