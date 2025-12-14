# Challenge 046: Reverse of a Number

def main():
    num = int(input("Enter number: "))
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reversed number:", reverse)


if __name__ == "__main__":
    main()
