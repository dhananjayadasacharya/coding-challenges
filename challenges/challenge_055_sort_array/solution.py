# Challenge 055: Sort & Search Level 2 (Sort asc/desc)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    choice = input("Enter a for ascending or d for descending: ")

    for i in range(n):
        for j in range(i + 1, n):
            if (choice == 'a' and arr[i] > arr[j]) or (choice == 'd' and arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

    print("Sorted array:", arr)


if __name__ == "__main__":
    main()
