# Challenge 049: Arrays Level 2 (Minimum value)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    min_val = arr[0]
    for x in arr:
        if x < min_val:
            min_val = x

    print("Minimum value:", min_val)


if __name__ == "__main__":
    main()
