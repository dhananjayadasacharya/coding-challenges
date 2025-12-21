# Challenge 059: 2D Arrays (Check element exists)

def main():
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    matrix = []

    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input("Enter element: ")))
        matrix.append(row)

    key = int(input("Enter element to search: "))
    found = False

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == key:
                found = True
                break

    if found:
        print("Element found")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
