# Challenge 058: 2D Arrays (Sum all elements)

def main():
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    matrix = []
    total = 0

    for i in range(r):
        row = []
        for j in range(c):
            val = int(input("Enter element: "))
            row.append(val)
            total += val
        matrix.append(row)

    print("Sum of all elements:", total)


if __name__ == "__main__":
    main()
