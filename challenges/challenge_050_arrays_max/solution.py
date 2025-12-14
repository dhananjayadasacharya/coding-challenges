# Challenge 050: Arrays Level 3 (Maximum value)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x

    print("Maximum value:", max_val)


if __name__ == "__main__":
    main()
