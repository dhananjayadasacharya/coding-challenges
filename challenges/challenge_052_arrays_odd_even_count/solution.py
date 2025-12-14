# Challenge 052: Arrays Level 5 (Count odd and even)

def main():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter element: ")))

    even = 0
    odd = 0

    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even count:", even)
    print("Odd count:", odd)


if __name__ == "__main__":
    main()
