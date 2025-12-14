# Challenge 045: Whole and Fraction Value Separation

def main():
    num = float(input("Enter a number: "))

    whole = int(num)
    fraction = num - whole

    print("Whole part:", whole)
    print("Fractional part:", fraction)


if __name__ == "__main__":
    main()
