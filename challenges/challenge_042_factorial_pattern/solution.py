# Challenge 042: Factorials Pattern (N Rows)
import math

def main():

    n = int(input("Enter number of rows: "))
    num = 1

    print(1)
    if n==1:
        quit()

    for i in range(2, n + 1):
        for j in range(i):
            print(math.factorial(num), end=" ")
            num += 1
        print()


if __name__ == "__main__":
    main()
