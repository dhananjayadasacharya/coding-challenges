# Challenge 054: Sort & Search Level 1 (Reverse array)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    rev = []
    for i in range(n - 1, -1, -1):
        rev.append(arr[i])

    print("Reversed array:", rev)


if __name__ == "__main__":
    main()
