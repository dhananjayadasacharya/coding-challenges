# Challenge 009: Check if a year is a leap year

def main():
    year = int(input("Enter a year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")
        

if __name__ == "__main__":
    main()
