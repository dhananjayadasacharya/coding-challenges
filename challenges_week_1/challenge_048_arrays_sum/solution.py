# Challenge 048: Arrays Level 1 (Sum of elements)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    total = 0
    for x in arr:
        total += x

    print("Sum of elements:", total)


if __name__ == "__main__":
    main()
