# Challenge 053: Sort & Search Level 0 (Input n and store elements)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    print("Array:", arr)


if __name__ == "__main__":
    main()
