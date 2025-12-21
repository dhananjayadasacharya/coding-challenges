# Challenge 044: Generate Series 1, -5, 9, -13, 17, -21, ... N

def main():
    n = int(input("Enter number of terms: "))

    value = 1
    sign = 1

    for i in range(n):
        print(value * sign, end=" ")
        value += 4
        sign *= -1


if __name__ == "__main__":
    main()
