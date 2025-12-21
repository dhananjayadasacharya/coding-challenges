# Challenge 051: Arrays Level 4 (Search element)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    key = int(input("Enter element to search: "))

    found = False
    for x in arr:
        if x == key:
            found = True
            break

    if found:
        print("Element found")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
