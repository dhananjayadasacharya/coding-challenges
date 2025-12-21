# Challenge 047: Arrays Level 0 (Input n and store elements)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        val = int(input("Enter element: "))
        arr.append(val)

    print("Array elements:", arr)


if __name__ == "__main__":
    main()
