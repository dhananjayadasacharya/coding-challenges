# Challenge 056: Sort & Search Level 3 (Binary Search)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    arr.sort()
    print("Sorted array:", arr)

    key = int(input("Enter element to search: "))

    low = 0
    high = n - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            found = True
            break
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if found:
        print("Element found")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
