# Challenge 010: Student Report Card Problem

def main():
    name = input("Enter student name: ")

    m1 = float(input("Enter marks in subject 1: "))
    m2 = float(input("Enter marks in subject 2: "))
    m3 = float(input("Enter marks in subject 3: "))

    total = m1 + m2 + m3
    average = total / 3

    print("Total Marks :", total)
    print("Average     :", average)

    if average >= 60:
        print("Class Secured: First Class")
    elif average >= 50:
        print("Class Secured: Second Class")
    elif average >= 35:
        print("Class Secured: Pass Class")
    else:
        print("Class Secured: Fail")


if __name__ == "__main__":
    main()
