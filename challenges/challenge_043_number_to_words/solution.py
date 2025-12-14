# Challenge 043: Convert Number to Words

def main():
    num = int(input("Enter number: "))

    words = ["Zero","One","Two","Three","Four",
            "Five","Six","Seven","Eight","Nine"]

    digits = []

    while num > 0:
        digits.append(num % 10)
        num //= 10

    digits.reverse()

    for d in digits:
        print(words[d], end=" ")


if __name__ == "__main__":
    main()
